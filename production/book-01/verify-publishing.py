#!/usr/bin/env python3
"""Validate offline publishing packets and preserve previously delivered story HTML."""
import base64
import hashlib
import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path

from publishing import publishing_replacements
from publishing_rules import validate_publishing_copy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nodes, self.stack = [], []

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "text": ""}
        self.nodes.append(node)
        if tag not in {"meta", "img", "image", "use", "rect", "br", "hr", "link", "input", "source", "wbr", "area", "base", "col", "embed", "param", "track"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, text):
        for node in self.stack:
            node["text"] += text

    def cls(self, name):
        return [n for n in self.nodes if name in n["attrs"].get("class", "").split()]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


baseline = json.loads((HERE / "publishing-batch-baseline.json").read_text())
reports = []
numbers = [int(n) for n in sys.argv[1:]] or list(range(2, 16))
for number in numbers:
    folder = HERE / f"ep-{number:03}"
    episode = json.loads((folder / "episode.json").read_text())
    pub = json.loads((folder / "publishing/publishing.json").read_text())
    validate_publishing_copy(pub)
    output = ROOT / f"episodes/book-01/ep-{number:03}.html"
    source = output.read_text()
    doc = Document()
    doc.feed(source)
    ids = [n["attrs"]["id"] for n in doc.nodes if "id" in n["attrs"]]
    assert len(ids) == len(set(ids)), (number, "duplicate id")
    assert all(not re.search(r"\s", i) for i in ids)
    by_id = {n["attrs"]["id"]: n for n in doc.nodes if "id" in n["attrs"]}
    for node in doc.nodes:
        for attr in ("href", "src"):
            value = node["attrs"].get(attr)
            if value is None:
                continue
            assert value.startswith(("#", "data:image/png;base64,")), (number, value[:80])
            if value.startswith("#"):
                assert value[1:] in by_id, (number, value)
    assert not re.search(r"@@[A-Z_]+@@|林一|林二|<(?:script|audio|video)\b", source, re.I)
    for name, count in (("scene", 8), ("word-card", len(episode["words"])), ("subtitle-item", episode["subtitle_pair_count"]), ("narration-block", 8), ("dialogue-reference", 8), ("publish-keyword", 30), ("publish-topic", len(pub["topics"])), ("publish-cover", 2), ("cover-download", 2)):
        assert len(doc.cls(name)) == count, (number, name)
    assert by_id["publish-title"]["text"] == pub["title"]
    assert by_id["publish-description"]["text"] == pub["description"]
    assert [n["text"] for n in doc.cls("publish-keyword")] == pub["keywords"]
    assert len(pub["keywords"]) == len(set(pub["keywords"])) == 30
    assert [n["text"] for n in doc.cls("publish-topic")] == ["#" + t for t in pub["topics"]]
    narration = [line for scene in episode["scenes"] for line in scene["narration"]]
    assert [n["text"] for n in doc.cls("voice-en")] == [n["en"] for n in narration]
    assert [n["text"] for n in doc.cls("caption-zh")] == [n["zh"] for n in narration]
    assert [n["id"] for n in narration] == [f"EN{i:03}" for i in range(1, len(narration) + 1)]
    for scene in episode["scenes"]:
        text = by_id[f'scene-{scene["id"]}']["text"]
        assert scene["action"] in text
        for cue in scene["cues"]:
            if cue.get("quiz"):
                continue
            for key in ("en", "zh") if "en" in cue else ("text",):
                assert cue[key] in text, (number, scene["id"], key)
    for word in episode["words"]:
        key = "word-" + word["word"].lower().replace(" ", "-")
        text = by_id[key]["text"]
        assert all(word[k] in text for k in ("word", "meaning", "expression", "translation"))
    assert base64.b64decode(by_id["storyboard-sheet"]["attrs"]["href"].split(",", 1)[1]) == (folder / "storyboard.png").read_bytes()
    for cover in pub["covers"]:
        image = (folder / "publishing" / cover["file"]).read_bytes()
        w, h = struct.unpack(">II", image[16:24])
        rw, rh = map(int, cover["id"].split("x"))
        assert w * rh == h * rw, (number, "cover ratio", w, h)
        preview = next(n for n in doc.nodes if n["tag"] == "img" and n["attrs"].get("alt") == cover["alt"])
        download = next(n for n in doc.cls("cover-download") if n["attrs"]["download"] == cover["download_name"])
        assert preview["attrs"]["src"] == download["attrs"]["href"]
        assert base64.b64decode(preview["attrs"]["src"].split(",", 1)[1]) == image
        assert (int(preview["attrs"]["width"]), int(preview["attrs"]["height"])) == (w, h)
    additions = publishing_replacements(folder)
    previous = source.replace(additions["PUBLISHING_CSS"], "", 1).replace(additions["PUBLISHING_SECTION"], "", 1).replace('<a href="#publishing">抖音发布</a>', "", 1)
    assert hashlib.sha256(previous.encode()).hexdigest() == baseline[str(output.relative_to(ROOT))], (number, "prior HTML changed outside publishing additions")
    for filename in ("episode.json", "storyboard.png"):
        path = folder / filename
        assert digest(path) == baseline[str(path.relative_to(ROOT))]
    report = {"episode": number, "checked_on": "2026-11-01", "status": "static-passed-browser-pending", "html": str(output.relative_to(ROOT)), "sha256": digest(output), "bytes": output.stat().st_size, "scenes": 8, "subtitle_pairs": len(narration), "learning_cards": len(episode["words"]), "vocabulary_mode": episode.get("vocabulary_mode", "new-and-review"), "topics": len(pub["topics"]), "unique_keywords": 30, "covers": [{"file": c["file"], "size": [c["width"], c["height"]], "ratio": c["id"], "sha256": c["sha256"]} for c in pub["covers"]], "original_story_html_preserved_exactly": True, "story_source_and_storyboard_unchanged": True, "preview_and_download_bytes_verified": True, "external_assets": [], "javascript_blocks": 0}
    (folder / "checks/publishing-verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    reports.append(report)
assert digest(ROOT / "episodes/book-01/ep-001.html") == baseline["episodes/book-01/ep-001.html"]
assert len(list((ROOT / "episodes/book-01").glob("*.html"))) == 15
(HERE / "publishing-batch-verification.json").write_text(json.dumps({"checked_on": "2026-11-01", "status": "static-passed-browser-pending", "updated_episodes": numbers, "episode_001_unchanged": True, "new_covers": len(reports) * 2, "reports": reports}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"static": "passed", "episodes": numbers, "covers": len(reports) * 2, "original_story_html_preserved_exactly": True}))
