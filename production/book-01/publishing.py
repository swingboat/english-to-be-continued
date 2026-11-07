"""Embed an episode's publishing copy and two PNG covers in its offline HTML."""
import base64
import html
import json
import struct
from pathlib import Path

from publishing_rules import validate_publishing_copy


def publishing_replacements(episode_dir):
    here = Path(episode_dir)
    shared = Path(__file__).resolve().parent
    episode = json.loads((here / "episode.json").read_text())
    data = json.loads((here / "publishing/publishing.json").read_text())
    validate_publishing_copy(data)
    assert data["episode"] == episode["id"]
    assert len(data["keywords"]) == len(set(data["keywords"])) == 30
    assert all(isinstance(k, str) and k.strip() == k and k for k in data["keywords"])
    assert len(data["topics"]) == len(set(data["topics"]))
    assert all(data[k].strip() for k in ("title", "description"))
    assert [c["id"] for c in data["covers"]] == ["4x3", "3x4"]
    esc = lambda v: html.escape(str(v), quote=True)
    covers = []
    for cover in data["covers"]:
        image = (here / "publishing" / cover["file"]).read_bytes()
        assert image[:8] == b"\x89PNG\r\n\x1a\n"
        width, height = struct.unpack(">II", image[16:24])
        assert (width, height) == (cover["width"], cover["height"])
        ratio_w, ratio_h = map(int, cover["id"].split("x"))
        assert width * ratio_h == height * ratio_w
        uri = "data:image/png;base64," + base64.b64encode(image).decode()
        covers.append(
            f'<figure class="publish-cover" id="publish-cover-{esc(cover["id"])}">'
            f'<div class="publish-cover-heading"><h4>{esc(cover["label"])}</h4>'
            f'<p>{width} × {height} · PNG</p></div>'
            f'<img src="{uri}" width="{width}" height="{height}" '
            f'alt="{esc(cover["alt"])}" loading="lazy" decoding="async">'
            f'<figcaption><a class="button cover-download" download="{esc(cover["download_name"])}" '
            f'href="{uri}">下载 {ratio_w}:{ratio_h} 封面 PNG</a></figcaption></figure>'
        )
    section = (shared / "publishing-section.template").read_text()
    fields = {
        "EPISODE": f'{episode["number"]:03}',
        "PUBLISH_TITLE": esc(data["title"]),
        "PUBLISH_DESCRIPTION": esc(data["description"]),
        "PUBLISH_TOPICS": " ".join(f'<span class="publish-topic">#{esc(t)}</span>' for t in data["topics"]),
        "PUBLISH_KEYWORDS": "，".join(f'<span class="publish-keyword">{esc(k)}</span>' for k in data["keywords"]),
        "PUBLISH_COVERS": "".join(covers),
    }
    for key, value in fields.items():
        section = section.replace("@@" + key + "@@", value)
    return {"PUBLISHING_CSS": (shared / "publishing.css").read_text(), "PUBLISHING_SECTION": section}
