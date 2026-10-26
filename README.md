# AI 需求分析助手 · 教学示例

> 这是《GitHub 协作实战》的配套演示仓库，用来展示从需求到发布的完整协作流程。仓库中的需求、代码与数据均为虚构，不对应任何真实客户。

## 项目要解决什么问题

产品经理每周要处理大量会议纪要、需求邮件和访谈记录。信息散落在文档里，难以追踪，也无法快速判断优先级。

本项目把这些材料整理成结构化的用户故事、验收标准与优先级建议，输出可以直接粘贴进 Issue 的 Markdown。

## 迭代 1 的范围

| 工作项 | 状态 | 负责人 |
| --- | --- | --- |
| 需求解析器 | 开发中 | @steiner020 |
| 用户故事模板 | 已完成 | @steiner020 |
| 验收标准生成 | 待开始 | 待认领 |
| 文档站 | 待开始 | 待认领 |

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.requirements_parser --input examples/meeting-notes.md
```

Windows 用户把第二行换成 `.venv\Scripts\activate`。

## 目录结构

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/     # Issue 表单
│   ├── workflows/          # CI 工作流
│   └── pull_request_template.md
├── docs/                   # 文档站
├── examples/               # 示例输入
├── prompts/                # 提示词模板
├── src/                    # 源代码
└── tests/                  # 测试
```

## 协作方式

1. 每个需求先开 Issue，并使用「需求」表单；没有 Issue 的改动不进入评审。
2. 分支命名：`feature/<issue 编号>-<简短描述>`，例如 `feature/2-story-parser`。
3. 提交信息遵循 Conventional Commits，例如 `feat(parser): 支持提取验收标准`。
4. PR 必须关联 Issue，并通过 CI 检查后才能合并。
5. 发布使用语义化版本，变更写入 Release Notes。

## 角色

| 角色 | 负责人 | 关注点 |
| --- | --- | --- |
| 项目经理 | 林澈 | 范围、排期、验收 |
| 算法工程师 | 阿岚 | 解析质量、评测集 |
| 前端工程师 | 小周 | 文档站与演示页 |
| 评审人 | 陈默 | 代码质量、可维护性 |

## 许可证

本项目使用 [MIT License](LICENSE)。示例数据均为虚构。
