# Airwallex 报告图表生成工具

用于为 `projects/airwallex-research/Airwallex全球调研报告.md` 生成可复用的数据图表。

## 使用方式

```bash
python3 utils/generate-airwallex-charts/generate_charts.py
```

默认输出目录：

```text
projects/airwallex-research/assets/charts/
```

脚本顶部的大写变量集中定义了输出目录、字体、配色和图表数据。需要更新公开数据时，优先修改脚本顶部的数据常量后重新运行。

