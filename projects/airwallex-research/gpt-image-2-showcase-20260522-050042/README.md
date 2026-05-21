# GPT-image-2 展示图生成准备

本目录用于生成 `Airwallex全球调研报告.gpt-image-2-20260522-050042.md` 对应的 GPT-image-2 展示图资产。

## 当前状态

已根据报告中的数据和表格生成 4 张 PNG 展示图，并复制到 `images/` 目录。当前生成使用 Codex 内置 `image_gen` 工具完成，不依赖 `OPENAI_API_KEY`。

已生成文件：

- `images/airwallex-ai-core-metrics-20260522-050042.png`
- `images/airwallex-ai-network-efficiency-20260522-050042.png`
- `images/airwallex-ai-europe-growth-20260522-050042.png`
- `images/airwallex-ai-revenue-streams-20260522-050042.png`

## GPT-image-2 CLI 备用命令

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/.system/imagegen/scripts/image_gen.py"

python "$IMAGE_GEN" generate-batch \
  --model gpt-image-2 \
  --input projects/airwallex-research/gpt-image-2-showcase-20260522-050042/prompts/showcase-prompts.jsonl \
  --out-dir projects/airwallex-research/gpt-image-2-showcase-20260522-050042/images \
  --quality high \
  --size 2048x1152 \
  --concurrency 3
```

## 精准性原则

AI 生成图片不适合单独承担关键数字和中文小字的最终数据层。为保证数据精准，最终发布时应以项目内现有 SVG 图表和正文为准确数据层，AI 输出用于增强展示感和视觉语境。
