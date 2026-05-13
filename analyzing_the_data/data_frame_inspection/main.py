import pandas as pd

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')

# Write your code below
column_names = wine_data.columns
data_types   = wine_data.dtypes

# Testing the result
print(column_names)
print(data_types)