from src.requirements_parser import parse_notes, render


def test_splits_stories_by_heading():
    text = "## 导入纪要\n- 支持 Markdown\n- 支持纯文本\n\n## 导出故事\n- 输出 Issue 草稿\n"
    stories = parse_notes(text)
    assert [story.title for story in stories] == ["导入纪要", "导出故事"]
    assert stories[0].notes == ["支持 Markdown", "支持纯文本"]


def test_ignores_bullets_before_first_heading():
    stories = parse_notes("- 开场白\n## 正文\n- 一条记录\n")
    assert len(stories) == 1
    assert stories[0].notes == ["一条记录"]


def test_supports_asterisk_bullets():
    stories = parse_notes("## 范围\n* 只处理文本\n")
    assert stories[0].notes == ["只处理文本"]


def test_render_adds_story_headings():
    output = render("## 登录\n- 支持邮箱登录\n")
    assert output.startswith("## 登录")
    assert "- 支持邮箱登录" in output


def test_render_without_headings_returns_hint():
    assert "没有识别到二级标题" in render("只有一段普通文字")


def test_blank_input_is_safe():
    assert parse_notes("") == []
