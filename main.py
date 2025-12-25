import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("population.csv")

# Set seaborn style
sns.set(style="whitegrid")

# -------- Histogram (Age Distribution) --------
plt.figure(figsize=(6,4))
sns.histplot(data["Age"], bins=5, kde=True, color="skyblue")
plt.title("Age Distribution of Population")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# -------- Bar Chart (Gender Distribution) --------
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=data, palette="pastel")
plt.title("Gender Distribution of Population")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
