#2. Find common elements between A and B. [Hint : Intersection of two sets]

import numpy as np

A = np.array([1, 2, 3, 4])
B = np.array([3, 4, 5])

common_elements = [int(element) for element in A if element in B]
print("Common elements between A and B:", common_elements)