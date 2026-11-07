#!/usr/bin/env python3
"""Check source copy limits and the actual delivered offline HTML."""
import json
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

from publishing_rules import validate_publishing_copy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class CopyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fields, self.topics, self.keywords = {}, [], []
        self.active = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "p" and attrs.get("id") in {"publish-title", "publish-description"}:
            self.active = attrs["id"]
            self.fields[self.active] = ""
        elif tag == "span" and attrs.get("class") in {"publish-topic", "publish-keyword"}:
            self.active = attrs["class"]
            (self.topics if self.active == "publish-topic" else self.keywords).append("")

    def handle_data(self, value):
        if self.active in self.fields:
            self.fields[self.active] += value
        elif self.active == "publish-topic":
            self.topics[-1] += value
        elif self.active == "publish-keyword":
            self.keywords[-1] += value

    def handle_endtag(self, tag):
        if tag in {"p", "span"}:
            self.active = None


def verify(folder):
    data = json.loads((folder / "publishing/publishing.json").read_text())
    metrics = validate_publishing_copy(data)
    parser = CopyParser()
    parser.feed((ROOT / "episodes/book-01" / (folder.name + ".html")).read_text())
    if parser.fields.get("publish-title") != data["title"] or parser.fields.get("publish-description") != data["description"]:
        raise ValueError("HTML 的标题或简介与源数据不一致")
    if parser.topics != ["#" + t for t in data["topics"]]:
        raise ValueError("HTML 话题与源数据不一致")
    keywords = [k.removesuffix("，") for k in parser.keywords]
    if keywords != data["keywords"] or len(keywords) != len(set(keywords)) or len(keywords) != 30:
        raise ValueError("必须保留 30 个不重复关键词，且 HTML 与源数据一致")
    return {"episode": data["episode"], "status": "passed", **metrics, "keywords": 30, "html_matches_source": True}


if __name__ == "__main__":
    folders = [HERE / f"ep-{int(n):03}" for n in sys.argv[1:]] if sys.argv[1:] else sorted(HERE.glob("ep-*/publishing/publishing.json"))
    folders = [p.parent.parent if p.name == "publishing.json" else p for p in folders]
    reports = []
    for folder in folders:
        try:
            reports.append(verify(folder))
        except (ValueError, KeyError, OSError) as error:
            reports.append({"episode": folder.name, "status": "failed", "error": str(error)})
    passed = bool(reports) and all(r["status"] == "passed" for r in reports)
    result = {"checked_on": datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat(), "status": "passed" if passed else "failed", "episodes": reports}
    (HERE / "publishing-limits-verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if passed else 1)
