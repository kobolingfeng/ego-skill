"""社交媒体自我分析器

分析你在社交媒体上发的内容，提取你的公开人设和私下真实状态之间的落差。

支持：
- 朋友圈截图（通过 Read 工具直接读取图片）
- 微博/小红书/ins 截图
- 导出的文本内容
"""

import argparse
import json
import re
from pathlib import Path
from collections import Counter


def parse_social_text(text: str) -> list[dict]:
    posts = []
    chunks = re.split(r"\n{2,}|---+", text.strip())

    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or len(chunk) < 5:
            continue

        date_match = re.search(
            r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})"
            r"|(\d{1,2}月\d{1,2}日)"
            r"|(\d+小时前|\d+分钟前|刚刚|昨天|前天)",
            chunk,
        )

        posts.append({
            "date": date_match.group(0) if date_match else None,
            "content": chunk,
            "length": len(chunk),
        })

    return posts


def analyze_posts(posts: list[dict]) -> dict:
    all_text = " ".join(p["content"] for p in posts)

    positive_words = ["开心", "快乐", "幸福", "哈哈", "太棒了", "喜欢", "爱", "好看", "好吃"]
    negative_words = ["累", "烦", "难过", "emo", "失眠", "焦虑", "不想", "无聊", "没意思"]

    pos_count = sum(all_text.count(w) for w in positive_words)
    neg_count = sum(all_text.count(w) for w in negative_words)

    late_night = 0
    for p in posts:
        if p["date"]:
            hour_match = re.search(r"(\d{2}):", p["date"])
            if hour_match and int(hour_match.group(1)) >= 23:
                late_night += 1

    return {
        "total_posts": len(posts),
        "avg_length": round(sum(p["length"] for p in posts) / len(posts), 1) if posts else 0,
        "tone_balance": {
            "positive_signals": pos_count,
            "negative_signals": neg_count,
            "ratio": f"{'偏积极' if pos_count > neg_count else '偏消极' if neg_count > pos_count else '平衡'}",
        },
        "late_night_posts": late_night,
        "sample_posts": [p["content"][:200] for p in posts[:10]],
    }


def main():
    parser = argparse.ArgumentParser(description="分析你的社交媒体内容")
    parser.add_argument("--file", required=True, help="社交媒体内容文件路径")
    parser.add_argument("--output", required=True, help="输出文件路径")
    args = parser.parse_args()

    path = Path(args.file)
    raw = path.read_text(encoding="utf-8")
    posts = parse_social_text(raw)
    analysis = analyze_posts(posts)
    analysis["source"] = str(path)

    Path(args.output).write_text(
        json.dumps(analysis, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"分析完成: {len(posts)} 条动态, 输出到 {args.output}")


if __name__ == "__main__":
    main()
