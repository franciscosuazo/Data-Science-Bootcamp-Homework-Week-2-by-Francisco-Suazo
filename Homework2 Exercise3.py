#3. Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]

import numpy as np

A = np.array([1, 3, 5, 7, 9, 11, 13, 15])

mask = (A >= 5) & (A <= 10)

numbers_in_range = A[mask]
print("Numbers between 5 and 10:", numbers_in_range)