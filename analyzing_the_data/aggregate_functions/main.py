import pandas as pd 

cars_data = {'model': ['audi A1', 'audi A6', 'audi A4', 'audi A3','audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'price': [12500, 16500, 16800, 17300, 16500]}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
highest_price = audi_cars['price'].max()
lowest_price = audi_cars['price'].min()
average_price = audi_cars['price'].mean()

# Testing the result
print(f'Highest price: {highest_price}, lowest price: {lowest_price}, average price: {average_price}')