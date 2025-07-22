from numpy import random
import numpy as np

a=random.randint(9)
b=random.randint(100, size=(3, 5))
print(a)
print(b)

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)  # Shuffle mean changing arrangement of elements in-place. i.e. in the array  itself
print(arr)

print(random.permutation(arr)) # The permutation() return a re-arranged array.


