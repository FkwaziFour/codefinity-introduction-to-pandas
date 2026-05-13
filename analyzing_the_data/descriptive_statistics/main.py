import pandas as pd

wine_data = pd.read_csv(
    "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/"
    "a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv"
)

# 1) mean of the 'residual sugar' column
residual_sugar_mean = wine_data["residual sugar"].mean()

# 2) mode of the 'fixed acidity' column
fixed_acidity_mode = wine_data["fixed acidity"].mode()[0]

# 3) full statistical overview
described_data = wine_data.describe()

# Testing the result
print(f"Residual sugar mean: {residual_sugar_mean}")
print(f"Fixed acidity mode: {fixed_acidity_mode}")
print(described_data)