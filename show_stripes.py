import pandas as pd
import matplotlib.pyplot as plt

# 1) Point to the CSV (either local path or the URL above)
url = "https://www.key2stats.com/EPICA_Dome_C_Ice_Core_800KYr_Temperature_Estimates_229_35.csv"

# 2) Load and subset to age (BP) and temperature anomaly dT
df = pd.read_csv(url, usecols=["Age","dT"])
df = df.dropna().sort_values("Age", ascending=True)

# 3) Normalize around zero for diverging colormap
vmax = df["dT"].abs().max()
vmin = -vmax
cmap = plt.get_cmap("RdBu_r")

# 4) Prepare a 2D array: one row, one column per sample
data = df["dT"].values.reshape(1, -1)

# 5) Plot
plt.figure(figsize=(12,1))
plt.imshow(data, aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax)
plt.axis("off")
plt.title("EPICA Dome C Temperature Anomalies (–800 kyr to present)")
plt.tight_layout()
plt.show()
