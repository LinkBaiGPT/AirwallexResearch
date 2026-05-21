from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch


# 输出图表目录，默认写回 Airwallex 项目资产目录。
OUTPUT_DIR = Path("projects/airwallex-research/assets/charts")

# 中文字体候选，优先使用 macOS 常见中文字体。
FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]

# 主色、强调色和中性色，保持报告商务风格。
COLOR_PRIMARY = "#1168D8"
COLOR_ACCENT = "#00A676"
COLOR_WARNING = "#F59E0B"
COLOR_DARK = "#172033"
COLOR_MUTED = "#667085"
COLOR_GRID = "#E6EAF0"
COLOR_BG = "#FFFFFF"

# Airwallex 2024/2025 核心增长数据，来自报告正文公开口径。
GROWTH_METRICS = [
    {"name": "ARR", "unit": "亿美元", "years": ["2024", "2025"], "values": [5.0, 10.0], "note": "+90% YoY"},
    {"name": "年化交易量", "unit": "亿美元", "years": ["2024", "2025"], "values": [1300, 2660], "note": "约翻倍"},
    {"name": "企业客户数", "unit": "万家+", "years": ["2024", "2025"], "values": [15, 20], "note": "20万+"},
    {"name": "估值", "unit": "亿美元", "years": ["2025.05", "2025.12"], "values": [62, 80], "note": "+约30%"},
]

# 交易网络效率与覆盖指标。
NETWORK_METRICS = [
    ("本地网络路由交易", 95, "%"),
    ("当日结算交易", 94, "%"),
    ("本地支付网络覆盖", 127, "国家"),
    ("可转账国家和地区", 207, "个"),
]

# 产品与基础设施覆盖变化。
COVERAGE_METRICS = [
    ("Global Account 覆盖国家", 65, 70, "国家"),
    ("钱包可持有币种", 22, 27, "种"),
    ("Local Transfer 覆盖", 118, 121, "国家"),
    ("SWIFT Transfer 覆盖", 150, 207, "国家/地区"),
]

# 欧洲与平台业务增速。
EUROPE_GROWTH = [
    ("EMEA 收入", 116),
    ("EMEA 交易量", 226),
    ("荷兰收入", 199),
    ("Connected accounts", 149),
]


def setup_style() -> None:
    for font_path in FONT_CANDIDATES:
        if Path(font_path).exists():
            font_manager.fontManager.addfont(font_path)
            plt.rcParams["font.family"] = font_manager.FontProperties(fname=font_path).get_name()
            break
    plt.rcParams.update(
        {
            "axes.unicode_minus": False,
            "figure.facecolor": COLOR_BG,
            "axes.facecolor": COLOR_BG,
            "savefig.facecolor": COLOR_BG,
            "svg.fonttype": "path",
            "font.size": 11,
        }
    )


def add_title(fig, title: str, subtitle: str) -> None:
    fig.text(0.055, 0.945, title, fontsize=20, fontweight="bold", color=COLOR_DARK)
    fig.text(0.055, 0.905, subtitle, fontsize=10.5, color=COLOR_MUTED)


def save_chart(fig, filename: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_DIR / filename, bbox_inches="tight")
    plt.close(fig)


def chart_growth_dashboard() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12.8, 8.2))
    add_title(fig, "Airwallex 核心经营指标进入规模化阶段", "2025 年收入、交易量、客户和估值同步上台阶；数据取自报告正文公开口径。")

    for ax, metric in zip(axes.flat, GROWTH_METRICS):
        values = metric["values"]
        bars = ax.bar(metric["years"], values, color=[COLOR_GRID, COLOR_PRIMARY], width=0.55)
        ax.set_title(metric["name"], loc="left", fontsize=13, fontweight="bold", color=COLOR_DARK, pad=12)
        ax.text(
            0.96,
            0.92,
            metric["note"],
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=10.5,
            color=COLOR_ACCENT,
            fontweight="bold",
        )
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.grid(axis="y", color=COLOR_GRID, linewidth=0.8)
        ax.tick_params(axis="y", length=0, labelcolor=COLOR_MUTED)
        ax.tick_params(axis="x", length=0, labelcolor=COLOR_DARK)
        ax.set_axisbelow(True)
        ymax = max(values) * 1.28
        ax.set_ylim(0, ymax)
        for bar, value in zip(bars, values):
            label = f"{value:g}{metric['unit']}"
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + ymax * 0.035,
                label,
                ha="center",
                va="bottom",
                fontsize=10.5,
                color=COLOR_DARK,
                fontweight="bold",
            )

    fig.text(0.055, 0.035, "注：ARR 2025 年为 10 亿美元+；交易量为年化口径；估值对比为 2025 年 F/G 轮。", fontsize=9.5, color=COLOR_MUTED)
    fig.tight_layout(rect=(0.045, 0.06, 0.98, 0.86), h_pad=2.7, w_pad=2.2)
    save_chart(fig, "airwallex-growth-dashboard.svg")


def chart_network_efficiency() -> None:
    fig, ax = plt.subplots(figsize=(12.8, 6.2))
    add_title(fig, "本地支付网络是 Airwallex 的效率杠杆", "95%+ 交易通过本地 rails 路由，94% 左右可当日结算；覆盖指标体现跨境资金调度广度。")
    ax.axis("off")

    cards = [
        (0.055, 0.56, 0.39, 0.24, "交易经本地网络路由", "95%+", COLOR_PRIMARY, "减少 SWIFT 和中间行依赖"),
        (0.515, 0.56, 0.39, 0.24, "交易可当日结算", "94%", COLOR_ACCENT, "提升到账确定性和客户体验"),
        (0.055, 0.20, 0.39, 0.24, "本地支付网络覆盖", "127", COLOR_WARNING, "国家"),
        (0.515, 0.20, 0.39, 0.24, "可转账国家和地区", "200+", COLOR_DARK, "Global transfer reach"),
    ]
    for x, y, w, h, label, value, color, note in cards:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.012,rounding_size=0.018",
            transform=fig.transFigure,
            linewidth=1,
            edgecolor=COLOR_GRID,
            facecolor="#F8FAFC",
        )
        fig.patches.append(patch)
        fig.text(x + 0.028, y + h - 0.065, label, fontsize=12, color=COLOR_MUTED)
        fig.text(x + 0.028, y + 0.075, value, fontsize=34, color=color, fontweight="bold")
        fig.text(x + 0.18, y + 0.092, note, fontsize=11, color=COLOR_DARK)

    fig.text(0.055, 0.055, "重点：效率指标越高，Airwallex 越能把传统跨境链路中的时间成本和中间行成本压缩为平台内部能力。", fontsize=10.5, color=COLOR_MUTED)
    save_chart(fig, "airwallex-network-efficiency.svg")


def chart_coverage_expansion() -> None:
    fig, ax = plt.subplots(figsize=(12.8, 6.8))
    add_title(fig, "产品覆盖从账户、钱包延伸到全球付款网络", "2025 年 Global Account、钱包币种和 SWIFT Transfer 覆盖继续扩展。")

    labels = [item[0] for item in COVERAGE_METRICS]
    old_values = [item[1] for item in COVERAGE_METRICS]
    new_values = [item[2] for item in COVERAGE_METRICS]
    units = [item[3] for item in COVERAGE_METRICS]
    y = range(len(labels))
    ax.barh(y, new_values, color="#DCEBFF", height=0.56, label="2025")
    ax.barh(y, old_values, color=COLOR_PRIMARY, height=0.34, label="此前口径")

    for i, (old, new, unit) in enumerate(zip(old_values, new_values, units)):
        ax.text(new + max(new_values) * 0.02, i, f"{old} → {new} {unit}", va="center", fontsize=10.5, color=COLOR_DARK, fontweight="bold")

    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
    ax.grid(axis="x", color=COLOR_GRID, linewidth=0.8)
    ax.tick_params(axis="y", length=0, labelcolor=COLOR_DARK)
    ax.tick_params(axis="x", length=0, labelcolor=COLOR_MUTED)
    ax.set_xlim(0, max(new_values) * 1.27)
    ax.legend(frameon=False, loc="lower right", labelcolor=COLOR_MUTED)
    fig.text(0.055, 0.055, "注：覆盖指标来自报告正文；不同产品口径不可直接相加，主要用于展示网络密度变化。", fontsize=9.5, color=COLOR_MUTED)
    fig.tight_layout(rect=(0.055, 0.08, 0.98, 0.86))
    save_chart(fig, "airwallex-coverage-expansion.svg")


def chart_europe_growth() -> None:
    fig, ax = plt.subplots(figsize=(12.8, 6.6))
    add_title(fig, "欧洲仍处于高速渗透期", "EMEA 交易量增速显著高于收入增速，说明 Airwallex 正用更大客户交易量扩大市场存在感。")

    labels = [item[0] for item in EUROPE_GROWTH]
    values = [item[1] for item in EUROPE_GROWTH]
    colors = [COLOR_PRIMARY, COLOR_ACCENT, COLOR_WARNING, "#7C3AED"]
    bars = ax.bar(labels, values, color=colors, width=0.58)
    ax.axhline(100, color=COLOR_GRID, linewidth=1.4)
    ax.text(3.45, 102, "100% 增长基准", ha="right", va="bottom", fontsize=9.5, color=COLOR_MUTED)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 8, f"+{value}%", ha="center", va="bottom", fontsize=13, fontweight="bold", color=COLOR_DARK)

    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="y", color=COLOR_GRID, linewidth=0.8)
    ax.tick_params(axis="y", length=0, labelcolor=COLOR_MUTED)
    ax.tick_params(axis="x", length=0, labelcolor=COLOR_DARK, labelsize=10.5)
    ax.set_ylim(0, max(values) * 1.22)
    ax.set_ylabel("同比增长", color=COLOR_MUTED)
    fig.text(0.055, 0.055, "注：荷兰收入增长为报告正文引用口径；connected accounts 为平台基础设施业务指标。", fontsize=9.5, color=COLOR_MUTED)
    fig.tight_layout(rect=(0.055, 0.08, 0.98, 0.86))
    save_chart(fig, "airwallex-europe-growth.svg")


def main() -> None:
    setup_style()
    chart_growth_dashboard()
    chart_network_efficiency()
    chart_coverage_expansion()
    chart_europe_growth()
    print(f"生成完成：{OUTPUT_DIR}")


if __name__ == "__main__":
    main()

