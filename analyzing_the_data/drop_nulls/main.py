import pandas as pd

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine_with_nan.csv')

# Write your code below
length_before = len(wine_data)
wine_data = wine_data.dropna()
length_after = len(wine_data)

# Testing the result
print(length_before - length_after)