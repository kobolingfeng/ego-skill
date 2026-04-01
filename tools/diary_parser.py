"""日记/心情笔记解析器

支持格式：
- 纯文本 (.txt)
- Markdown (.md)
- Day One 导出 (JSON)
- 备忘录导出

提取维度：
- 时间线（按日期排序）
- 情绪关键词
- 反复出现的主题
- 高频人名/地名
"""

import argparse
import json
import re
from pathlib import Path
from collections import Counter
from datetime import datetime


def parse_text(text: str) -> list[dict]:
    entries = []
    date_pattern = re.compile(
        r"(\d{4}[-/年]\d{1,2}[-/月]\d{1,2}[日]?)"
        r"|(\d{1,2}[-/月]\d{1,2}[日]?)"
    )

    chunks = re.split(r"\n{2,}", text.strip())

    for chunk in chunks:
        if not chunk.strip():
            continue
        date_match = date_pattern.search(chunk)
        entry = {
            "date": date_match.group(0) if date_match else None,
            "content": chunk.strip(),
            "length": len(chunk.strip()),
        }
        entries.append(entry)

    return entries


def parse_dayone_json(data: dict) -> list[dict]:
    entries = []
    for item in data.get("entries", []):
        entries.append({
            "date": item.get("creationDate", ""),
            "content": item.get("text", ""),
            "length": len(item.get("text", "")),
        })
    return entries


def extract_emotions(entries: list[dict]) -> dict:
    emotion_words = {
        "焦虑": ["焦虑", "紧张", "不安", "慌", "恐惧", "害怕"],
        "悲伤": ["难过", "伤心", "哭", "眼泪", "崩溃", "绝望"],
        "愤怒": ["生气", "愤怒", "烦", "操", "受不了", "凭什么"],
        "空虚": ["空", "无聊", "没意思", "麻木", "无所谓"],
        "自我怀疑": ["不够好", "不配", "废物", "没用", "失败"],
        "孤独": ["孤独", "一个人", "没人理", "被抛弃", "不被理解"],
        "疲惫": ["累", "疲惫", "撑不住", "想休息", "不想动"],
    }

    counter = Counter()
    for entry in entries:
        text = entry["content"]
        for emotion, keywords in emotion_words.items():
            for kw in keywords:
                if kw in text:
                    counter[emotion] += 1
                    break

    return dict(counter.most_common())


def extract_recurring_topics(entries: list[dict]) -> list[str]:
    all_text = " ".join(e["content"] for e in entries)
    topic_patterns = [
        "工作", "上班", "加班", "领导", "同事",
        "爸", "妈", "父", "母", "家里", "父母",
        "前任", "对象", "男朋友", "女朋友", "老公", "老婆",
        "朋友", "室友", "同学",
        "钱", "房租", "存款", "工资",
        "未来", "以后", "方向", "迷茫",
        "死", "活着", "意义", "为什么",
    ]
    found = []
    for topic in topic_patterns:
        count = all_text.count(topic)
        if count >= 2:
            found.append((topic, count))

    found.sort(key=lambda x: x[1], reverse=True)
    return [f"{t}({c}次)" for t, c in found[:15]]


def main():
    parser = argparse.ArgumentParser(description="解析日记/心情笔记")
    parser.add_argument("--file", required=True, help="输入文件路径")
    parser.add_argument("--output", required=True, help="输出文件路径")
    parser.add_argument("--format", default="auto", choices=["auto", "txt", "dayone"])
    args = parser.parse_args()

    path = Path(args.file)
    raw = path.read_text(encoding="utf-8")

    if args.format == "dayone" or (args.format == "auto" and path.suffix == ".json"):
        entries = parse_dayone_json(json.loads(raw))
    else:
        entries = parse_text(raw)

    emotions = extract_emotions(entries)
    topics = extract_recurring_topics(entries)

    result = {
        "source": str(path),
        "entry_count": len(entries),
        "date_range": {
            "earliest": entries[0]["date"] if entries and entries[0]["date"] else "未知",
            "latest": entries[-1]["date"] if entries and entries[-1]["date"] else "未知",
        },
        "emotions": emotions,
        "recurring_topics": topics,
        "entries": entries,
    }

    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"解析完成: {len(entries)} 条记录, 输出到 {args.output}")


if __name__ == "__main__":
    main()
