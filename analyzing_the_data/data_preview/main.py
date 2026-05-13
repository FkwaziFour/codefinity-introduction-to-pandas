import pandas as pd
import numpy as np

# This line ensures that the results are reproducible
np.random.seed(5)

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')

# Write your code below
first_lines = wine_data.head(10)
last_lines = wine_data.tail(15)
random_rows = wine_data.sample(12)

# Testing the result
print(first_lines)
print(last_lines)
print(random_rows)