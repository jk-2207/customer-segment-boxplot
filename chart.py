import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Synthetic customer purchase data for different segments
# ---------------------------------------------------------

# Random seed for reproducibility
np.random.seed(42)

segments = ["Budget", "Regular", "Premium", "VIP"]
n_customers_per_segment = 150

data = []

for segment in segments:
    if segment == "Budget":
        # Lower spend, tighter spread
        purchases = np.random.lognormal(mean=2.5, sigma=0.35, size=n_customers_per_segment)
    elif segment == "Regular":
        purchases = np.random.lognormal(mean=3.0, sigma=0.4, size=n_customers_per_segment)
    elif segment == "Premium":
        purchases = np.random.lognormal(mean=3.5, sigma=0.45, size=n_customers_per_segment)
    else:  # VIP
        purchases = np.random.lognormal(mean=4.0, sigma=0.5, size=n_customers_per_segment)

    # Add a few high-spend outliers per segment
    outliers = np.random.choice([0, 0, 0, 1], size=n_customers_per_segment)
    purchases = purchases + outliers * np.random.uniform(300, 800, size=n_customers_per_segment)

    for amt in purchases:
        data.append({"Customer_Segment": segment, "Purchase_Amount": amt})

df = pd.DataFrame(data)

# ---------------------------------------------------------
# Seaborn styling (professional look)
# ---------------------------------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")  # suitable for presentations

# ---------------------------------------------------------
# Create the figure and boxplot
# ---------------------------------------------------------

# 8x8 inches with dpi=64 → 512x512 pixels
plt.figure(figsize=(8, 8))

ax = sns.boxplot(
    data=df,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="viridis"
)

ax.set_title(
    "Customer Purchase Amount Distribution by Segment",
    pad=16,
    fontsize=18
)
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Purchase Amount ($)")

# Rotate x-axis labels slightly for readability
plt.xticks(rotation=10)

# Tight layout for clean spacing
plt.tight_layout()

# ---------------------------------------------------------
# Save chart as 512x512 PNG
# ---------------------------------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()