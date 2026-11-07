#!/usr/bin/env python3
"""Build episode 007 as one offline script, picture and vocabulary HTML."""
import base64
import html
import json
import re
import struct
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE.parent))
from publishing import publishing_replacements
data = json.loads((HERE / "episode.json").read_text())
image = (HERE / "storyboard.png").read_bytes()
assert image[:8] == b"\x89PNG\r\n\x1a\n"
width, height = struct.unpack(">II", image[16:24])


def esc(value):
    return html.escape(str(value), quote=True)


targets = {}
for word in data["words"]:
    for form in [word["word"], *word.get("forms", [])]:
        targets[form.lower()] = "word-" + word["word"].replace(" ", "-")
for word in [*data["review_words"], *data["supplemental_review_words"]]:
    targets[word["word"].lower()] = "review-" + word["word"].replace(" ", "-")
pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(targets, key=len, reverse=True)) + r")\b", re.I)


def mark(value):
    return pattern.sub(lambda m: f'<a class="keyword" href="#{targets[m[0].lower()]}">{m[0]}</a>', esc(value))


def art(panel, label):
    box = " ".join(str(v) for v in data["art"]["panels"][panel])
    return f'<svg viewBox="{box}" preserveAspectRatio="xMidYMid meet" role="img" aria-label="{esc(label)}"><use href="#storyboard-sheet" clip-path="url(#panel-clip-{panel})"/></svg>'


contents, scripts = [], []
for scene in data["scenes"]:
    number = scene["id"]
    contents.append(f'<a href="#scene-{number}" class="scene-link"><span>{number:02}</span>{esc(scene["name"])}</a>')
    lines = []
    for cue in scene["cues"]:
        if "en" in cue:
            text = f'<span class="dialogue-en" lang="en">{mark(cue["en"])}</span><span class="dialogue-zh">{esc(cue["zh"])}</span>'
        else:
            text = esc(cue["text"])
        lines.append(f'<li><span class="speaker">{esc(cue["who"])}</span><span class="dialogue-text">{text}</span></li>')
    table = ""
    if "table" in scene:
        t = scene["table"]
        head = "".join(f'<th scope="col">{esc(c)}</th>' for c in t["columns"])
        body = "".join('<tr>'+"".join(f'<th scope="row">{esc(v)}</th>' if i == 0 else f'<td>{esc(v)}</td>' for i, v in enumerate(row))+'</tr>' for row in t["rows"])
        table = f'<div class="table-wrap"><table><caption>{esc(t["caption"])}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    narration_lines = []
    for line in scene["narration"]:
        narration_lines.append(f'<li class="subtitle-item" id="subtitle-{esc(line["id"])}"><span class="caption-index">{esc(line["id"])}</span><div class="caption-text"><p class="voice-en" lang="en">{mark(line["en"])}</p><p class="caption-zh" lang="zh-CN">{esc(line["zh"])}</p></div></li>')
    narration = '<section class="narration-block" aria-label="本格英文解说及中英字幕"><h4>英文解说 · 中英字幕</h4><ol class="subtitle-list">'+"".join(narration_lines)+'</ol></section>'
    scripts.append(f'<article class="scene" id="scene-{number}" aria-labelledby="scene-title-{number}"><div class="scene-heading"><span class="scene-number">{number:02}</span><div><p class="scene-place">{esc(scene["place"])}</p><h3 id="scene-title-{number}">{esc(scene["name"])}</h3></div></div><div class="scene-body"><figure class="scene-picture">{art(scene["panel"], scene["shot"])}<figcaption>分镜 {number:02} / {esc(scene["name"])}</figcaption></figure><div class="scene-script"><p class="action"><strong>动作</strong>{esc(scene["action"])}</p>{narration}<details class="dialogue-reference"><summary>角色对白参考</summary><ol class="dialogue">{"".join(lines)}</ol></details>{table}<details class="direction"><summary>分镜说明</summary><p>{esc(scene["shot"])}</p><p><strong>音效参考：</strong>{esc(scene["sound"])}</p></details></div></div></article>')

cards = []
for index, word in enumerate(data["words"], 1):
    cards.append(f'<article class="word-card" id="word-{esc(word["word"].replace(" ", "-"))}" aria-labelledby="word-title-{index}"><div class="word-top"><span class="word-number">WORD / {index:02}</span><a class="scene-reference" href="#scene-{word["scene"]}">故事第 {word["scene"]} 格 ↗</a></div><h3 id="word-title-{index}" lang="en">{esc(word["word"])}</h3><p class="meaning"><span>{esc(word["part"])}</span>{esc(word["meaning"])}</p><blockquote lang="en">{esc(word["expression"])}</blockquote><p class="example-zh">{esc(word["translation"])}</p><p class="word-usage">{esc(word["usage"])}</p><p class="story-question">想一想：{esc(word["question"])}</p><p class="word-source">{esc(word["source"])}</p></article>')
review = []
for word in data["review_words"]:
    review.append(f'<div class="review-item" id="review-{esc(word["word"].replace(" ", "-"))}"><p><strong lang="en">{esc(word["word"])}</strong>{esc(word["meaning"])}</p><p class="review-example" lang="en">{esc(word["expression"])}</p><p>{esc(word["translation"])}</p><a href="#scene-{word["scene"]}">回到故事第 {word["scene"]} 格</a></div>')

supplemental = []
for word in data["supplemental_review_words"]:
    supplemental.append(f'<div class="review-item supplemental-review-item" id="review-{esc(word["word"].replace(" ", "-"))}"><p><strong lang="en">{esc(word["word"])}</strong>{esc(word["meaning"])}</p><p>{esc(word["question"])}</p><details><summary>查看参考答案</summary><p class="review-example" lang="en">{esc(word["expression"])}</p><p>{esc(word["translation"])}</p></details></div>')

replacements = {
    "PANEL_CLIPS": "".join(f'<clipPath id="panel-clip-{i}" clipPathUnits="userSpaceOnUse"><rect x="{b[0]}" y="{b[1]}" width="{b[2]}" height="{b[3]}"/></clipPath>' for i, b in enumerate(data["art"]["panels"])),
    "SHEET_URI": "data:image/png;base64," + base64.b64encode(image).decode(),
    "SHEET_WIDTH": str(width), "SHEET_HEIGHT": str(height),
    "COVER_ART": art(3, "试机没声音，分身指向另一个小帅，希望他来签名；小帅低头看着那张分工表。"),
    "CONTENTS": "".join(contents), "SCRIPT_SCENES": "".join(scripts),
    "WORD_CARDS": "".join(cards),
    "WORD_LINKS": "".join(f'<a href="#word-{esc(w["word"].replace(" ", "-"))}" lang="en">{esc(w["word"])}</a>' for w in data["words"]),
    "REVIEW_WORDS": '<aside class="review-block" aria-labelledby="review-title"><h3 id="review-title">前面学过的词，这次自己用</h3><div class="review-grid">'+"".join(review)+'</div></aside>',
    "SUPPLEMENTAL_REVIEW": '<details class="continuity supplemental-review"><summary>课后再想一想：5 个到期旧词</summary><p>先回想第五集，再展开参考答案。</p><div class="review-grid">'+"".join(supplemental)+'</div></details>',
    "CONTINUITY_END": "".join(f'<li>{esc(x)}</li>' for x in data["continuity"]["end"]),
    "CONTINUITY_PROPS": "".join(f'<li>{esc(x)}</li>' for x in data["continuity"]["props"]),
}
replacements.update(publishing_replacements(HERE))
template = (HERE / "page.template").read_text()
for key, value in replacements.items():
    template = template.replace("@@" + key + "@@", value)
assert not re.search(r"@@[A-Z_]+@@", template)
assert len(data["scenes"]) == 8 and len(data["art"]["panels"]) == 8
assert all(s.get("narration") and all(x.get("en") and x.get("zh") for x in s["narration"]) for s in data["scenes"])
assert {w["word"] for w in data["words"]} == {"responsible", "be responsible for", "function", "seek", "professional"}
assert not re.search(r"<(?:script|video|audio)\b", template, flags=re.I)
out = ROOT / "episodes/book-01/ep-007.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(template)
print(json.dumps({"output": str(out), "bytes": out.stat().st_size, "scenes": 8, "words": 5, "dialogue_entries": sum(len(s["cues"]) for s in data["scenes"]), "format": "reading-html", "offline": True}, ensure_ascii=False))
