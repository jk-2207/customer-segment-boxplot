import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------------
# Generate synthetic data
# -------------------------------

np.random.seed(42)
segments = ["Budget", "Regular", "Premium", "VIP"]
n = 150

data = []

for s in segments:
    if s == "Budget":
        base = np.random.normal(40, 8, n)
    elif s == "Regular":
        base = np.random.normal(70, 15, n)
    elif s == "Premium":
        base = np.random.normal(120, 25, n)
    else:  # VIP
        base = np.random.normal(200, 40, n)

    data.extend([{"Customer_Segment": s, "Purchase_Amount": x} for x in base])

df = pd.DataFrame(data)

# -------------------------------
# Plot (any size is fine)
# -------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))
sns.boxplot(data=df, x="Customer_Segment", y="Purchase_Amount", palette="viridis")
plt.title("Customer Purchase Amount Distribution by Segment")
plt.xticks(rotation=10)
plt.tight_layout()

# Save temporary version
plt.savefig("chart_temp.png", dpi=100)
plt.close()

# -------------------------------
# FORCE EXACT 512x512 IMAGE
# -------------------------------

temp = Image.open("chart_temp.png")

# Create final canvas
final = Image.new("RGB", (512, 512), "white")

# Resize plot to fit within 512, keeping aspect ratio
temp = temp.resize((512, 512), Image.LANCZOS)

# Paste into final canvas (center)
final.paste(temp, (0, 0))

# Save final EXACT 512×512
final.save("chart.png")