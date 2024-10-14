#1. Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print (a)
print (b)

x1=np.vstack((a,b))
print (x1)

x2=np.hstack((a,b))
print (x2)