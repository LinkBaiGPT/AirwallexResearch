# GPT-image-2 展示图生成准备

本目录用于生成 `Airwallex全球调研报告.gpt-image-2-20260522-050042.md` 对应的 GPT-image-2 展示图资产。

## 当前状态

当前环境缺少 `OPENAI_API_KEY`，因此尚未执行真实 GPT-image-2 生成。已准备好提示词文件和输出目录，密钥配置好后可直接运行。

## 运行命令

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

GPT-image-2 不适合直接承担关键数字和中文小字的最终数据层。为保证数据精准，提示词要求生成专业展示底图和版式感，不要求模型自由改写数字。最终发布时应以项目内现有 SVG 图表作为准确数据层，GPT-image-2 输出用于增强展示感和视觉语境。

