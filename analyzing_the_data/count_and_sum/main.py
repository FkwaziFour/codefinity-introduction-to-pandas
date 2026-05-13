import pandas as pd 

cars_data = {'model': [None, 'audi A6', 'audi A4', None,'audi A1'],
             'year': [2017, 2016, 2017, None, 2016],
             'fueltype': [None, 'diesel', 'diesel', 'petrol', 'petrol'],
             'price': [12500, 16500, 16800, 17300, 16500]}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
number_of_cells = audi_cars.count()
total_price       = audi_cars['price'].sum()
null_count        = audi_cars.isna().sum()

# Testing the result
print('Missing values:')
print(null_count)
print('Number of non-null cells:')
print(number_of_cells)
print(f'Total price: {total_price}')