"""Shared limits for the current Douyin web video publishing packet."""
import json
from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parents[2] / "data/douyin-publishing-policy.json"
POLICY = json.loads(POLICY_PATH.read_text())


def text_units(value):
    """Conservatively count supplementary characters as two units."""
    return len(value.encode("utf-16-le")) // 2


def validate_publishing_copy(data):
    """Fail before rendering; topics share the description's 1000-unit budget."""
    for key in ("title", "description"):
        value = data.get(key)
        if not isinstance(value, str) or not value or value != value.strip():
            raise ValueError(f"{key} 必须为非空文本，且首尾无空白")
        if "#" in value:
            raise ValueError(f"{key} 不内联话题，请使用 topics 字段")
    if "\n" in data["title"] or "\r" in data["title"]:
        raise ValueError("title 必须为单行")
    topics = data.get("topics")
    if not isinstance(topics, list) or not 1 <= len(topics) <= POLICY["topics_max"]:
        raise ValueError(f"topics 必须为 1—{POLICY['topics_max']} 个话题")
    if any(not isinstance(t, str) or not t or "#" in t or any(c.isspace() for c in t) for t in topics):
        raise ValueError("topics 必须为不含 # 和空白的非空话题名称")
    if len(topics) != len(set(topics)):
        raise ValueError("topics 不得重复")
    title_length = text_units(data["title"])
    if title_length > POLICY["title_max_units"]:
        raise ValueError(f"标题 {title_length} 字，超过 {POLICY['title_max_units']} 字上限")
    caption = data["description"] + "\n" + " ".join("#" + t for t in topics)
    caption_length = text_units(caption)
    if caption_length > POLICY["description_with_topics_max_units"]:
        raise ValueError(f"简介含话题 {caption_length} 字，超过 {POLICY['description_with_topics_max_units']} 字上限")
    return {
        "title_units": title_length,
        "description_units": text_units(data["description"]),
        "description_with_topics_units": caption_length,
        "topics": len(topics),
        "policy_checked_on": POLICY["checked_on"],
    }
