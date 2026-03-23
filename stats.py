import pandas as pd

# Load dataset (online CSV)
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Print dataset shape
print("Dataset Shape:", data.shape)

# Print column names
print("\nColumn Names:")
print(data.columns)

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# First 5 rows
print("\nFirst 5 rows:")
print(data.head())
data = pd.read_csv("iris.csv")