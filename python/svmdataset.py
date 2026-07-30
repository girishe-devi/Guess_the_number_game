import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("iris_dataset.csv")

# Scatter Plot
plt.scatter(
    df["SepalLengthCm"],
    df["SepalWidthCm"]
)

# Labels and Title
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Scatter Plot")

# Show Plot
plt.show()