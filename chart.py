import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# ---------------------------------------------------------
# Synthetic customer purchase data by segment
# ---------------------------------------------------------
np.random.seed(42)

segments = ["Budget", "Regular", "Premium", "VIP"]
n_customers_per_segment = 150

data = []

for segment in segments:
    if segment == "Budget":
        purchases = np.random.lognormal(mean=2.5, sigma=0.35, size=n_customers_per_segment)
    elif segment == "Regular":
        purchases = np.random.lognormal(mean=3.0, sigma=0.4, size=n_customers_per_segment)
    elif segment == "Premium":
        purchases = np.random.lognormal(mean=3.5, sigma=0.45, size=n_customers_per_segment)
    else:
        purchases = np.random.lognormal(mean=4.0, sigma=0.5, size=n_customers_per_segment)

    # Add occasional outliers
    outliers = np.random.choice([0, 0, 0, 1], size=n_customers_per_segment)
    purchases += outliers * np.random.uniform(300, 800, size=n_customers_per_segment)

    for amt in purchases:
        data.append({"Customer_Segment": segment, "Purchase_Amount": amt})

df = pd.DataFrame(data)

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ---------------------------------------------------------
# Create boxplot (any size is fine now)
# ---------------------------------------------------------
plt.figure(figsize=(8, 8))  # initial canvas (not final size)
ax = sns.boxplot(
    data=df,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="viridis"
)

ax.set_title("Customer Purchase Amount Distribution by Segment", pad=16)
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Purchase Amount ($)")
plt.xticks(rotation=10)
plt.tight_layout()

# Save temporary chart
plt.savefig("chart_temp.png", dpi=100)
plt.close()

# ---------------------------------------------------------
# FORCE FINAL OUTPUT TO EXACTLY 512x512 PIXELS
# ---------------------------------------------------------
img = Image.open("chart_temp.png")
final_img = img.resize((512, 512), Image.LANCZOS)
final_img.save("chart.png")