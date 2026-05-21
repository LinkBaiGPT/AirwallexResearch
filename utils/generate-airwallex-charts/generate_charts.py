from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


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

# 盈利公式拆解。
PROFIT_FORMULA_ITEMS = [
    ("企业客户数", "20万+ 企业客户", COLOR_PRIMARY),
    ("单客户交易量", "2660亿美元年化交易量", COLOR_ACCENT),
    ("产品渗透率", "半数以上客户使用多产品", COLOR_WARNING),
    ("Take Rate", "FX / 交易费 / 卡 / 软件 / Yield", "#7C3AED"),
    ("清算与合规成本", "本地 rails 降成本，合规是固定成本", COLOR_MUTED),
]

# 收入结构表对应图。
REVENUE_STREAMS = [
    ("跨境支付与 FX", "付款 / 收款 / 换汇", "价格竞争"),
    ("收单与本地支付", "卡收单 / 本地支付方式", "Stripe / Adyen"),
    ("企业卡与 Spend", "虚拟卡 / 报销 / 审批", "本地费用管理"),
    ("嵌入式金融", "API / 分账 / 钱包", "平台稳定性"),
    ("Billing", "订阅 / 发票 / 应收", "成熟 SaaS 玩家"),
    ("Yield / Treasury", "闲置资金管理", "利率与监管"),
]

# 产品路径四层。
PRODUCT_LAYERS = [
    ("资金入口", "全球账户 / 本地收款 / 线上收单", "抢占企业资金流入口", COLOR_PRIMARY),
    ("资金调拨", "跨境付款 / 批量付款 / FX", "替代传统银行跨境汇款", COLOR_ACCENT),
    ("资金使用", "企业卡 / 支出管理 / 报销审批", "进入企业日常运营", COLOR_WARNING),
    ("资金智能化", "Billing / Yield / Embedded Finance / AI Agents", "升级为金融云", "#7C3AED"),
]

# 全球化阶段。
GLOBALIZATION_STAGES = [
    ("2015-2017", "痛点验证", "从咖啡馆跨境采购痛点切入"),
    ("2017-2020", "基础设施转向", "API 驱动跨境支付基础设施"),
    ("2020-2024", "全球牌照扩张", "客户数突破 15 万，ARR 超 5 亿美元"),
    ("2025-至今", "规模化与智能化", "ARR 破 10 亿美元，AI Agents 加速"),
]

# 竞争格局。
COMPETITION_MAP = [
    ("线上收单", "Stripe / Adyen / Mollie", "收单资金接入多币种账户"),
    ("跨境汇款", "Wise / Revolut / 银行", "更深 API、审批和平台能力"),
    ("企业卡费用", "Brex / Ramp / Qonto", "绑定多币种余额降低 FX 损耗"),
    ("平台分账", "Stripe Connect / Adyen", "服务跨国平台钱包与出金"),
    ("企业银行", "HSBC / Citi / JPMorgan", "覆盖中型数字化企业空白"),
]

# Nubank 对比。
NUBANK_COMPARISON = [
    ("客户类型", "C 端个人与小微", "B2B 企业与平台"),
    ("起点产品", "无年费信用卡", "跨境支付和外汇"),
    ("核心壁垒", "用户规模 / 信用数据", "牌照 / 本地网络 / API"),
    ("盈利逻辑", "活跃用户 × ARPAC", "企业资金流 × 产品渗透"),
    ("最大风险", "信贷周期", "合规与系统可靠性"),
    ("终局形态", "拉美数字金融平台", "全球企业金融操作系统"),
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
    fig.savefig(OUTPUT_DIR / filename, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def wrap(text: str, width: int = 18) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False))


def fig_card(fig, x: float, y: float, w: float, h: float, face: str = "#F8FAFC", edge: str = COLOR_GRID) -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        transform=fig.transFigure,
        linewidth=1,
        edgecolor=edge,
        facecolor=face,
    )
    fig.patches.append(patch)


def fig_arrow(fig, start: tuple[float, float], end: tuple[float, float], color: str = COLOR_GRID) -> None:
    arrow = FancyArrowPatch(
        start,
        end,
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.2,
        color=color,
    )
    fig.patches.append(arrow)


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


def chart_profit_formula() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 5.6))
    add_title(fig, "Airwallex 盈利公式：规模、渗透与成本控制同时作用", "表格中的变量可以理解为一条从客户规模到平台盈利能力的价值链。")
    ax.axis("off")

    xs = [0.055, 0.235, 0.415, 0.595, 0.775]
    y = 0.35
    w = 0.145
    h = 0.30
    for i, (label, detail, color) in enumerate(PROFIT_FORMULA_ITEMS):
        fig_card(fig, xs[i], y, w, h)
        fig.text(xs[i] + 0.018, y + h - 0.07, label, fontsize=12.5, color=COLOR_DARK, fontweight="bold")
        fig.text(xs[i] + 0.018, y + 0.13, wrap(detail, 12), fontsize=10, color=COLOR_MUTED, linespacing=1.35)
        fig.text(xs[i] + 0.018, y + 0.045, "驱动项" if i < 4 else "成本项", fontsize=10.5, color=color, fontweight="bold")
        if i < len(xs) - 1:
            operator = "×" if i < 3 else "−"
            fig.text(xs[i] + w + 0.012, y + 0.145, operator, fontsize=24, color=COLOR_MUTED, fontweight="bold")
            fig_arrow(fig, (xs[i] + w + 0.035, y + 0.15), (xs[i + 1] - 0.015, y + 0.15))

    fig_card(fig, 0.28, 0.13, 0.44, 0.10, face="#EEF6FF", edge="#C9E1FF")
    fig.text(0.305, 0.165, "平台盈利能力 = 企业客户数 × 单客户交易量 × 产品渗透率 × Take Rate − 清算 / FX / 合规 / 服务成本", fontsize=11, color=COLOR_DARK, fontweight="bold")
    fig.text(0.055, 0.045, "重点：Airwallex 的长期毛利空间，来自自建网络降低边际成本，以及多产品使用提升客户价值。", fontsize=10, color=COLOR_MUTED)
    save_chart(fig, "airwallex-profit-formula.svg")


def chart_revenue_streams() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 8.0))
    add_title(fig, "收入结构正在从交易型走向金融软件型", "六类收入来源共同构成 Airwallex 的货币化路径，风险主要来自费率压缩、竞争和监管。")
    ax.axis("off")

    positions = [(0.055, 0.58), (0.37, 0.58), (0.685, 0.58), (0.055, 0.27), (0.37, 0.27), (0.685, 0.27)]
    colors = [COLOR_PRIMARY, COLOR_ACCENT, COLOR_WARNING, "#7C3AED", "#0F766E", "#B45309"]
    for (x, y), (name, source, risk), color in zip(positions, REVENUE_STREAMS, colors):
        fig_card(fig, x, y, 0.255, 0.22)
        fig.text(x + 0.02, y + 0.155, name, fontsize=13, color=COLOR_DARK, fontweight="bold")
        fig.text(x + 0.02, y + 0.100, wrap(source, 16), fontsize=10.2, color=COLOR_MUTED)
        fig.text(x + 0.02, y + 0.045, f"风险：{risk}", fontsize=10.2, color=color, fontweight="bold")

    fig_card(fig, 0.22, 0.08, 0.56, 0.10, face="#F2F8F5", edge="#CDE8DA")
    fig.text(0.245, 0.118, "迁移方向：一次性交易费  →  企业卡 / 平台 / Billing / Treasury / AI 自动化等更高粘性收入", fontsize=11, color=COLOR_DARK, fontweight="bold")
    save_chart(fig, "airwallex-revenue-streams.svg")


def chart_product_stack() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 7.6))
    add_title(fig, "产品路径：从资金入口堆叠到智能财务操作系统", "表格中的四层能力不是并列功能，而是围绕同一套账户和账本逐层加深。")
    ax.axis("off")

    x = 0.15
    w = 0.70
    h = 0.115
    ys = [0.25, 0.39, 0.53, 0.67]
    for idx, ((name, ability, meaning, color), y) in enumerate(zip(PRODUCT_LAYERS, ys)):
        fig_card(fig, x, y, w, h, face="#F8FAFC")
        fig.text(x + 0.025, y + 0.072, name, fontsize=14, color=color, fontweight="bold")
        fig.text(x + 0.20, y + 0.073, ability, fontsize=11.2, color=COLOR_DARK)
        fig.text(x + 0.20, y + 0.030, meaning, fontsize=10.2, color=COLOR_MUTED)
        if idx < len(ys) - 1:
            fig_arrow(fig, (0.50, y + h + 0.01), (0.50, ys[idx + 1] - 0.012), color="#BCD2EA")

    fig.text(0.15, 0.16, "阅读方式：越往上，Airwallex 越接近企业财务工作台；越往下，越接近支付和账户基础设施。", fontsize=10.5, color=COLOR_MUTED)
    save_chart(fig, "airwallex-product-stack.svg")


def chart_globalization_timeline() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 6.4))
    add_title(fig, "全球化路径：从痛点工具到金融基础设施平台", "Airwallex 的关键变化，是从前端工具逐步转向牌照、网络、API 和 AI 自动化。")
    ax.axis("off")

    y = 0.46
    x_positions = [0.08, 0.315, 0.55, 0.785]
    for idx, ((period, stage, detail), x) in enumerate(zip(GLOBALIZATION_STAGES, x_positions)):
        fig_card(fig, x, y, 0.17, 0.23)
        fig.text(x + 0.018, y + 0.165, period, fontsize=11, color=COLOR_PRIMARY, fontweight="bold")
        fig.text(x + 0.018, y + 0.115, stage, fontsize=13, color=COLOR_DARK, fontweight="bold")
        fig.text(x + 0.018, y + 0.045, wrap(detail, 13), fontsize=9.7, color=COLOR_MUTED, linespacing=1.3)
        if idx < len(x_positions) - 1:
            fig_arrow(fig, (x + 0.18, y + 0.115), (x_positions[idx + 1] - 0.012, y + 0.115), color="#BCD2EA")

    fig_card(fig, 0.18, 0.18, 0.64, 0.11, face="#EEF6FF", edge="#C9E1FF")
    fig.text(0.205, 0.222, "主线：跨境支付痛点验证 → API 基础设施 → 全球牌照网络 → 规模化、盈利拐点与 AI 财务自动化", fontsize=11, color=COLOR_DARK, fontweight="bold")
    save_chart(fig, "airwallex-globalization-timeline.svg")


def chart_competition_map() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 8.0))
    add_title(fig, "竞争格局：Airwallex 面对的是一整套金融工具栈", "一体化优势来自跨模块联动，而不是在每个单点上都替代垂直冠军。")
    ax.axis("off")

    x_left, x_mid, x_right = 0.065, 0.39, 0.70
    y0, gap = 0.70, 0.115
    fig.text(x_left, 0.80, "业务环节", fontsize=12, color=COLOR_MUTED, fontweight="bold")
    fig.text(x_mid, 0.80, "主要竞争者", fontsize=12, color=COLOR_MUTED, fontweight="bold")
    fig.text(x_right, 0.80, "Airwallex 的竞争逻辑", fontsize=12, color=COLOR_MUTED, fontweight="bold")
    for idx, (segment, rivals, logic) in enumerate(COMPETITION_MAP):
        y = y0 - idx * gap
        fig_card(fig, x_left, y, 0.22, 0.075, face="#F8FAFC")
        fig_card(fig, x_mid, y, 0.22, 0.075, face="#FFFFFF")
        fig_card(fig, x_right, y, 0.24, 0.075, face="#F2F8F5", edge="#CDE8DA")
        fig.text(x_left + 0.015, y + 0.028, segment, fontsize=11, color=COLOR_DARK, fontweight="bold")
        fig.text(x_mid + 0.015, y + 0.028, wrap(rivals, 22), fontsize=9.3, color=COLOR_MUTED)
        fig.text(x_right + 0.015, y + 0.028, wrap(logic, 18), fontsize=9.3, color=COLOR_DARK)
        fig_arrow(fig, (x_left + 0.235, y + 0.038), (x_mid - 0.012, y + 0.038), color="#D1DCEB")
        fig_arrow(fig, (x_mid + 0.235, y + 0.038), (x_right - 0.012, y + 0.038), color="#D1DCEB")

    fig.text(0.065, 0.065, "重点：Airwallex 的强项不是单点最低价，而是把收款、账户、付款、卡、费用和平台能力放进同一账本。", fontsize=10.5, color=COLOR_MUTED)
    save_chart(fig, "airwallex-competition-map.svg")


def chart_nubank_comparison() -> None:
    fig, ax = plt.subplots(figsize=(13.6, 8.2))
    add_title(fig, "Nubank vs Airwallex：同是金融数字化，规模来源不同", "Nubank 抓个人金融频次，Airwallex 抓全球企业资金流和企业工作流。")
    ax.axis("off")

    fig_card(fig, 0.11, 0.17, 0.34, 0.62, face="#F8FAFC")
    fig_card(fig, 0.55, 0.17, 0.34, 0.62, face="#EEF6FF", edge="#C9E1FF")
    fig.text(0.24, 0.735, "Nubank", fontsize=20, color="#7C3AED", fontweight="bold", ha="center")
    fig.text(0.72, 0.735, "Airwallex", fontsize=20, color=COLOR_PRIMARY, fontweight="bold", ha="center")

    y = 0.66
    for label, nubank, airwallex in NUBANK_COMPARISON:
        fig.text(0.49, y, label, fontsize=10.5, color=COLOR_MUTED, fontweight="bold", ha="center")
        fig.text(0.135, y, wrap(nubank, 14), fontsize=10.2, color=COLOR_DARK, ha="left")
        fig.text(0.575, y, wrap(airwallex, 15), fontsize=10.2, color=COLOR_DARK, ha="left")
        y -= 0.078

    fig.text(0.11, 0.075, "共同点：不是简单用“更便宜”赢，而是用数字化重构传统金融服务的成本结构和触达方式。", fontsize=10.5, color=COLOR_MUTED)
    save_chart(fig, "airwallex-nubank-comparison.svg")


def main() -> None:
    setup_style()
    chart_growth_dashboard()
    chart_profit_formula()
    chart_revenue_streams()
    chart_network_efficiency()
    chart_product_stack()
    chart_coverage_expansion()
    chart_globalization_timeline()
    chart_competition_map()
    chart_europe_growth()
    chart_nubank_comparison()
    print(f"生成完成：{OUTPUT_DIR}")


if __name__ == "__main__":
    main()
