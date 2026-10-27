"""把会议纪要整理成用户故事草稿。

这是一个刻意保持简单的教学示例：不调用模型，只用规则演示
“输入 → 解析 → 结构化输出”的流水线，方便测试与截图。
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Story:
    """一条待确认的用户故事。"""

    title: str
    notes: list[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        bullets = "\n".join(f"- {note}" for note in self.notes)
        return f"## {self.title}\n\n{bullets}\n"


def parse_notes(text: str) -> list[Story]:
    """按二级标题拆分纪要，并收集标题下的列表项。"""
    stories: list[Story] = []
    current: Story | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        heading = re.match(r"^#{2,3}\s+(.+)$", line)
        if heading:
            current = Story(title=heading.group(1).strip())
            stories.append(current)
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        if bullet and current is not None:
            current.notes.append(bullet.group(1).strip())

    return stories


def render(text: str) -> str:
    """输出可直接粘贴进 Issue 的 Markdown。"""
    stories = parse_notes(text)
    if not stories:
        return "> 没有识别到二级标题，请先补充结构。\n"
    return "\n".join(story.to_markdown() for story in stories)


def main() -> None:
    parser = argparse.ArgumentParser(description="把会议纪要转换为用户故事草稿")
    parser.add_argument("path", type=Path, help="Markdown 格式的会议纪要")
    args = parser.parse_args()
    print(render(args.path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
