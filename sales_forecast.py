from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent

CHART_FILE = BASE_DIR / "sales_chart.png"


def create_chart(sales):

    month_names = [
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"
    ]

    used_months = month_names[:len(sales)]

    plt.figure(figsize=(10,5))

    plt.plot(
        used_months,
        sales,
        marker="o",
        linewidth=3
    )

    plt.fill_between(
        used_months,
        sales,
        alpha=0.2
    )

    plt.title("Sales Forecast Analysis")

    plt.xlabel("Months")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(CHART_FILE)

    plt.close()