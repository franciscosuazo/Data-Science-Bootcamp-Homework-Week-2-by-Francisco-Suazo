#From df filter the 'Manufacturer', 'Model' and 'Type' for every
#20th row starting from 1st (row 0).
#```
#df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
#```

import pandas as pd

cars93 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered_rows = cars93.iloc[::20][['Manufacturer', 'Model', 'Type']]

print(filtered_rows)