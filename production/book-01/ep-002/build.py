#!/usr/bin/env python3
"""Build episode 002 as one offline script, picture and vocabulary HTML."""
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
voice_root = ROOT / "voices/book-01"
cast = json.loads((voice_root / "cast.json").read_text())
voices = {v["name"]: v for v in cast["voices"]}
image = (HERE / "storyboard.png").read_bytes()
assert image[:8] == b"\x89PNG\r\n\x1a\n"
width, height = struct.unpack(">II", image[16:24])


def esc(value):
    return html.escape(str(value), quote=True)


targets = {}
for word in data["words"]:
    for form in [word["word"], *word.get("forms", [])]:
        targets[form.lower()] = "word-" + word["word"]
for word in data["review_words"]:
    targets[word["word"]] = "review-" + word["word"]
pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(targets, key=len, reverse=True)) + r")\b", re.I)


def mark(value):
    return pattern.sub(lambda m: f'<a class="keyword" href="#{targets[m[0].lower()]}">{m[0]}</a>', esc(value))


def art(panel, label):
    x, y, w, h = data["art"]["panels"][panel]
    style = f'aspect-ratio:{w}/{h};background-size:{width/w*100:.8f}% {height/h*100:.8f}%;background-position:{x/(width-w)*100:.8f}% {y/(height-h)*100:.8f}%'
    return f'<div class="panel-raster" role="img" aria-label="{esc(label)}" style="{style}"></div>'


cast_cards = []
for index, member in enumerate(data["voice_cast"], 1):
    voice = voices[member["name"]]
    selection = voice.get("selection", {})
    status = "待确认"
    if selection.get("status") == "selected":
        status = "暂定采用" if selection.get("provisional") else "已选定"
    paths = {}
    for kind, suffix in (("audio", "wav"), ("text", "txt")):
        relative = selection.get(f"reference_{kind}", f'characters/{voice["name"]}/{voice["name"]}.{suffix}')
        path = voice_root / relative
        assert path.is_file(), f"Missing voice reference: {path}"
        paths[kind] = path.relative_to(ROOT).as_posix()
    rows = [
        ("性别 / 年龄感", f'{voice["gender"]} · {voice["age"]} 岁左右'),
        ("性格", voice["personality"]),
        ("音色特征", voice["direction_zh"]),
        ("本集用途", member["usage"]),
    ]
    details = "".join(f'<div><dt>{esc(label)}</dt><dd>{esc(value)}</dd></div>' for label, value in rows)
    references = "".join(
        f'<div><dt>{label}</dt><dd><strong>{esc(Path(paths[kind]).name)}</strong><code>{esc(paths[kind])}</code></dd></div>'
        for kind, label in (("audio", "参考语音"), ("text", "对应文本"))
    )
    note = "用户已确认，先使用当前音色。" if status == "暂定采用" else (
        "用户已确认使用。" if status == "已选定" else "参考语音已生成，尚未获得用户音色确认。"
    )
    audio_bytes = (ROOT / paths["audio"]).read_bytes()
    audio_uri = "data:audio/wav;base64," + base64.b64encode(audio_bytes).decode()
    audition_text = (ROOT / paths["text"]).read_text().strip()
    cast_cards.append(
        f'<article class="cast-card" id="cast-{index}" aria-labelledby="cast-name-{index}">'
        f'<div class="cast-listen"><h3 id="cast-name-{index}">{esc(voice["name"])}</h3>'
        f'<p class="voice-status" data-status="{esc(status)}">{esc(status)}</p>'
        f'<audio controls preload="none" aria-label="播放{esc(voice["name"])}的参考语音" src="{audio_uri}">请使用支持音频播放的浏览器。</audio>'
        f'<p class="cast-note">人物音色参考 · 英文试听</p></div>'
        f'<div class="cast-profile"><dl class="cast-details">{details}</dl>'
        f'<details class="voice-files"><summary>试听文本与参考文件</summary><blockquote lang="en">{esc(audition_text)}</blockquote>'
        f'<dl class="cast-details">{references}</dl></details></div></article>'
    )


contents, scripts = [], []
for scene in data["scenes"]:
    number = scene["id"]
    contents.append(f'<a href="#scene-{number}" class="scene-link">{esc(scene["name"])}</a>')
    lines = []
    for cue in scene["cues"]:
        assert all(name in voices for name in cue["voices"])
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
        kind = {"narration": "英文解说 · 小帅", "retold_dialogue": "解说转述 · " + line.get("quoted_character", ""), "inner_monologue": "内心独白转述 · 小帅"}[line["kind"]]
        narration_lines.append(f'<li class="subtitle-item" id="subtitle-{esc(line["id"])}"><span class="caption-index">{esc(line["id"])}</span><div class="caption-text"><p class="caption-kind">{esc(kind)}</p><p class="voice-en" lang="en">{mark(line["en"])}</p><p class="caption-zh" lang="zh-CN">{esc(line["zh"])}</p></div></li>')
    direction = scene["voice_direction"]
    narration_direction = f'<p class="narration-direction"><strong>解说声音：小帅</strong>{esc(direction["narration"])}</p>'
    if direction.get("inner_monologue"):
        narration_direction += f'<p class="narration-direction"><strong>内心独白</strong>{esc(direction["inner_monologue"])}</p>'
    role_directions = '<dl class="role-directions">' + "".join(
        f'<div><dt>{esc(item["name"])}</dt><dd>{esc(item["direction"])}</dd></div>' for item in direction["dialogue"]
    ) + '</dl>'
    narration = '<section class="narration-block" aria-label="本格英文解说及中英字幕"><h4>英文解说 · 中英字幕</h4>'+narration_direction+'<ol class="subtitle-list">'+"".join(narration_lines)+'</ol></section>'
    scripts.append(f'<li><article class="scene" id="scene-{number}" aria-labelledby="scene-title-{number}"><div class="scene-heading"><h3 id="scene-title-{number}">{esc(scene["name"])}</h3><p class="scene-place">{esc(scene["place"])}</p></div><div class="scene-body"><figure class="scene-picture">{art(scene["panel"], scene["shot"])}<figcaption>分镜 {number} · {esc(scene["name"])}</figcaption></figure><div class="scene-script"><p class="action"><strong>动作</strong>{esc(scene["action"])}</p>{narration}<details class="dialogue-reference"><summary>角色对白参考 · 人物语气</summary><p class="dialogue-note">对白由对应人物音色录制，以下内容供后续视频项目参考；英文解说中的引语仍由小帅转述。</p>{role_directions}<ol class="dialogue">{"".join(lines)}</ol></details>{table}<details class="direction"><summary>分镜说明</summary><p>{esc(scene["shot"])}</p><p><strong>音效参考：</strong>{esc(scene["sound"])}</p></details></div></div></article></li>')

cards = []
for index, word in enumerate(data["words"], 1):
    cards.append(f'<article class="word-card" id="word-{esc(word["word"])}" aria-labelledby="word-title-{index}"><div class="word-definition"><h3 id="word-title-{index}" lang="en">{esc(word["word"])}</h3><p class="meaning"><span>{esc(word["part"])}</span>{esc(word["meaning"])}</p><a class="scene-reference" href="#scene-{word["scene"]}">回到第 {word["scene"]} 格</a></div><div class="word-context"><blockquote lang="en">{esc(word["expression"])}</blockquote><p class="example-zh">{esc(word["translation"])}</p><p class="word-usage">{esc(word["usage"])}</p><p class="story-question">想一想：{esc(word["question"])}</p><p class="word-source">{esc(word["source"])}</p></div></article>')
review = []
for word in data["review_words"]:
    review.append(f'<div class="review-item" id="review-{esc(word["word"])}"><p><strong lang="en">{esc(word["word"])}</strong>{esc(word["meaning"])}</p><p class="review-example" lang="en">{esc(word["expression"])}</p><p>{esc(word["translation"])}</p><a href="#scene-{word["scene"]}">回到故事第 {word["scene"]} 格</a></div>')

replacements = {
    "PANEL_CLIPS": "".join(f'<clipPath id="panel-clip-{i}" clipPathUnits="userSpaceOnUse"><rect x="{b[0]}" y="{b[1]}" width="{b[2]}" height="{b[3]}"/></clipPath>' for i, b in enumerate(data["art"]["panels"])),
    "SHEET_URI": "data:image/png;base64," + base64.b64encode(image).decode(),
    "SHEET_WIDTH": str(width), "SHEET_HEIGHT": str(height),
    "COVER_ART": art(0, "苏小满看着两个小帅，要求他们先交清活动确认表。"),
    "CONTENTS": "".join(contents), "SCRIPT_SCENES": "".join(scripts),
    "CAST_CARDS": "".join(cast_cards),
    "SUBTITLE_COUNT": str(data["subtitle_pair_count"]),
    "WORD_CARDS": "".join(cards),
    "WORD_LINKS": "".join(f'<a href="#word-{esc(w["word"])}" lang="en">{esc(w["word"])}</a>' for w in data["words"]),
    "REVIEW_WORDS": '<aside class="review-block" aria-labelledby="review-title"><h3 id="review-title">上集的词，这次自己用</h3><div class="review-grid">'+"".join(review)+'</div></aside>',
    "CONTINUITY_END": "".join(f'<li>{esc(x)}</li>' for x in data["continuity"]["end"]),
    "CONTINUITY_PROPS": "".join(f'<li>{esc(x)}</li>' for x in data["continuity"]["props"]),
}
replacements.update(publishing_replacements(HERE))
replacements["PUBLISHING_SECTION"] = re.sub(r'<p class="kicker">.*?</p>', '', replacements["PUBLISHING_SECTION"])
replacements["PUBLISHING_SECTION"] = replacements["PUBLISHING_SECTION"].replace('</span>，<span class="publish-keyword">', '，</span><span class="publish-keyword">')
publishing_hint = re.search(r'<p class="publishing-hint">.*?</p>', replacements["PUBLISHING_SECTION"])
if publishing_hint:
    section = replacements["PUBLISHING_SECTION"].replace(publishing_hint[0], "")
    position = section.rfind('</section>')
    replacements["PUBLISHING_SECTION"] = section[:position] + publishing_hint[0] + section[position:]
replacements["FONT_CSS"] = "\n".join(
    '@font-face{font-family:"Schibsted Grotesk";font-style:normal;font-weight:'+str(weight)+';font-display:swap;src:url(data:font/ttf;base64,'+base64.b64encode((HERE / f"assets/schibsted-grotesk-{weight}.ttf").read_bytes()).decode()+') format("truetype");}'
    for weight in (400, 600, 800)
)
replacements["PAGE_CSS"] = (HERE / "page.css").read_text()
replacements["PAGE_JS"] = (HERE / "page.js").read_text()
template = (HERE / "page.template").read_text()
for key, value in replacements.items():
    template = template.replace("@@" + key + "@@", value)
assert not re.search(r"@@[A-Z_]+@@", template)
assert len(data["scenes"]) == 8 and len(data["art"]["panels"]) == 8
assert all(s.get("narration") and all(x.get("en") and x.get("zh") for x in s["narration"]) for s in data["scenes"])
assert {w["word"] for w in data["words"]} == {"stressful", "challenging", "arise", "expectation", "pressure"}
assert not re.search(r"<video\b", template, flags=re.I)
assert template.count('<audio ') == len(data["voice_cast"])
out = ROOT / "episodes/book-01/ep-002.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(template)
print(json.dumps({"output": str(out), "bytes": out.stat().st_size, "scenes": 8, "words": 5, "dialogue_entries": sum(len(s["cues"]) for s in data["scenes"]), "format": "reading-html", "offline": True}, ensure_ascii=False))
