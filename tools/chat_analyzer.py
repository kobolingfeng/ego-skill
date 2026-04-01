"""聊天记录自我分析器

分析用户自己发出的消息，提取：
- 你的表达模式（不是对方的）
- 你在什么时候最活跃/最沉默
- 你在对话中扮演什么角色
- 你的情绪高频词

支持格式：
- 微信导出 (WeChatMsg / 留痕 / PyWxDump)
- QQ 导出 (txt / mht)
- 纯文本粘贴
"""

import argparse
import json
import re
from pathlib import Path
from collections import Counter


def parse_wechat_txt(text: str, my_name: str) -> list[dict]:
    messages = []
    pattern = re.compile(
        r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+"
        r"(.+?)\n"
        r"([\s\S]*?)(?=\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}|$)"
    )

    for match in pattern.finditer(text):
        timestamp, sender, content = match.groups()
        is_mine = my_name.lower() in sender.lower() or sender.strip() == "我"
        messages.append({
            "timestamp": timestamp.strip(),
            "sender": sender.strip(),
            "content": content.strip(),
            "is_mine": is_mine,
        })

    return messages


def parse_plain_text(text: str) -> list[dict]:
    messages = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        messages.append({
            "timestamp": None,
            "sender": "我",
            "content": line,
            "is_mine": True,
        })
    return messages


def analyze_my_messages(messages: list[dict]) -> dict:
    my_msgs = [m for m in messages if m["is_mine"]]
    if not my_msgs:
        return {"error": "没有找到你发的消息"}

    all_text = " ".join(m["content"] for m in my_msgs)

    avg_len = sum(len(m["content"]) for m in my_msgs) / len(my_msgs)

    emotion_words = {
        "焦虑": ["焦虑", "紧张", "不安", "慌", "怎么办"],
        "悲伤": ["难过", "伤心", "哭", "不开心", "崩溃"],
        "愤怒": ["生气", "烦", "受不了", "凭什么", "操"],
        "疲惫": ["累", "困", "不想动", "好累", "撑不住"],
        "自我怀疑": ["不够好", "不配", "我是不是", "我怎么这么"],
        "讨好": ["不好意思", "麻烦你了", "对不起", "我可以", "没关系的"],
    }
    emotion_counter = Counter()
    for emotion, keywords in emotion_words.items():
        for kw in keywords:
            count = all_text.count(kw)
            if count > 0:
                emotion_counter[emotion] += count

    question_marks = all_text.count("？") + all_text.count("?")
    exclamation_marks = all_text.count("！") + all_text.count("!")
    ellipsis = all_text.count("…") + all_text.count("...")

    hour_counter = Counter()
    for m in my_msgs:
        if m["timestamp"]:
            hour_match = re.search(r"(\d{2}):\d{2}:\d{2}", m["timestamp"])
            if hour_match:
                hour_counter[int(hour_match.group(1))] += 1

    return {
        "total_messages": len(my_msgs),
        "avg_message_length": round(avg_len, 1),
        "emotions": dict(emotion_counter.most_common()),
        "punctuation": {
            "question_marks": question_marks,
            "exclamation_marks": exclamation_marks,
            "ellipsis": ellipsis,
        },
        "active_hours": dict(hour_counter.most_common(5)),
        "sample_messages": [m["content"] for m in my_msgs[:20]],
    }


def main():
    parser = argparse.ArgumentParser(description="分析聊天记录中你自己的消息")
    parser.add_argument("--file", required=True, help="聊天记录文件路径")
    parser.add_argument("--name", default="我", help="你在聊天记录中的名字")
    parser.add_argument("--output", required=True, help="输出文件路径")
    parser.add_argument("--format", default="auto", choices=["auto", "wechat", "plain"])
    args = parser.parse_args()

    path = Path(args.file)
    raw = path.read_text(encoding="utf-8")

    if args.format == "wechat" or (args.format == "auto" and ":" in raw[:200]):
        messages = parse_wechat_txt(raw, args.name)
    else:
        messages = parse_plain_text(raw)

    analysis = analyze_my_messages(messages)
    analysis["source"] = str(path)
    analysis["my_name"] = args.name

    Path(args.output).write_text(
        json.dumps(analysis, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"分析完成: {analysis.get('total_messages', 0)} 条你的消息, 输出到 {args.output}")


if __name__ == "__main__":
    main()
