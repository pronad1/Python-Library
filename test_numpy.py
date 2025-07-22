import numpy as np

print(np.__version__)
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))
arr=np.array([[[1,2, 3], [4,5, 6], [7,8, 9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(arr.ndim)
print(arr.shape)
print(arr)
print(arr[1,0,0])  # access the first element of the first array of the second array
print(arr[1,0,-1]) # access the last element of the first array of the second array
print('index 1,0,-1 to 0,1,-3', arr[1, 0, ::-1].tolist() + arr[0, 2, ::-1].tolist() + arr[0, 1, ::-1].tolist())


# filer
arr = np.array([41, 42, 43, 44])
x = arr[[True, False, True, False]]
print(x)

filter_arr = arr > 42
na= arr[filter_arr]
print(filter_arr)
print(na)

