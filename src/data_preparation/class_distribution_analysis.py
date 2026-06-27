import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT /
    "dataset/reports/statistics_report/class_distribution.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT /
    "dataset/reports/eda_report/class_distribution"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

imbalance_results = []

datasets = df["dataset"].unique()

for dataset_name in datasets:

    dataset_df = df[df["dataset"] == dataset_name]

    # ==========================
    # BAR CHART
    # ==========================

    plt.figure(figsize=(12, 6))

    plt.bar(
        dataset_df["class"],
        dataset_df["image_count"]
    )

    plt.xticks(rotation=90)

    plt.title(
        f"{dataset_name} Class Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR /
        f"{dataset_name.lower()}_bar_chart.png",
        dpi=300
    )

    plt.close()

    # ==========================
    # PIE CHART
    # ==========================

    if len(dataset_df) <= 20:

        plt.figure(figsize=(8, 8))

        plt.pie(
            dataset_df["image_count"],
            labels=dataset_df["class"],
            autopct="%1.1f%%"
        )

        plt.title(
            f"{dataset_name} Class Distribution"
        )

        plt.savefig(
            OUTPUT_DIR /
            f"{dataset_name.lower()}_pie_chart.png",
            dpi=300
        )

        plt.close()

    # ==========================
    # IMBALANCE REPORT
    # ==========================

    max_count = dataset_df["image_count"].max()
    min_count = dataset_df["image_count"].min()

    ratio = round(max_count / min_count, 2)

    if ratio < 2:
        status = "Balanced"
    elif ratio < 5:
        status = "Moderately Imbalanced"
    else:
        status = "Severely Imbalanced"

    imbalance_results.append({
        "dataset": dataset_name,
        "max_class_count": max_count,
        "min_class_count": min_count,
        "imbalance_ratio": ratio,
        "status": status
    })

# ==========================
# SAVE REPORT
# ==========================

imbalance_df = pd.DataFrame(
    imbalance_results
)

imbalance_df.to_csv(
    OUTPUT_DIR / "imbalance_report.csv",
    index=False
)

print("\nClass Distribution Analysis Completed")
print(imbalance_df)