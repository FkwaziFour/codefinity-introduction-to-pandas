import pandas as pd

cars_data = {'model': ['audi A1', 'audi A6', 'audi A4', 'audi A3','audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'capital': ['Manila', 'Monaco', 'Bangkok', 'Stockhol', 'Valletta']}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
unique_years = audi_cars['year'].unique()
unique_fueltype = audi_cars['fueltype'].unique()
count_unique_fueltypes = audi_cars['fueltype'].nunique()

# Testing the result
print(unique_years)
print(unique_fueltype)
print(count_unique_fueltypes)