'''
Replace missing values in Min.Price and Max.Price columns with
their respective mean.
```
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```
'''

import pandas as pd

cars93 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

new_cars93 = cars93.copy()
new_cars93['Min.Price'] = new_cars93['Min.Price'].fillna(new_cars93['Min.Price'].mean())
new_cars93['Max.Price'] = new_cars93['Max.Price'].fillna(new_cars93['Max.Price'].mean())

print(new_cars93[['Min.Price', 'Max.Price']].isnull().sum())
print(new_cars93)