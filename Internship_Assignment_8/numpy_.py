import numpy as np

print("(4x2) NumPy array with random values:")
arr1 = np.random.rand(4, 2)
print(arr1)
print()

print("(3x5) Empty NumPy array (contains uninitialized data):")
arr2 = np.empty((3, 5))
print(arr2)
print()

print("(3x5) NumPy array filled with all zeros:")
arr3 = np.zeros((3, 5))
print(arr3)
print()

print("(4x3x2) NumPy array filled with all ones:")
arr4 = np.ones((4, 3, 2))
print(arr4)
print()

print("(3x3) 2D matrix with values ranging from 2 to 10:")
arr5 = np.arange(2, 11).reshape((3, 3))
print(arr5)
print()

arr6 = np.zeros(10)
print("Original null vector of size 10:")
print(arr6)
arr6[5] = 11
print("Null vector after updating the sixth value to 11:")
print(arr6)
print()

arr7 = np.array([1, 2, 3, 4, 5])
print("Original array:")
print(arr7)
arr8 = arr7[::-1]
print("Reversed array (first element becomes last):")
print(arr8)
print()

arr9 = np.array([1, 2, 3, 4, 5], dtype = np.float32)
print("Array created directly as float32 type:")
print(arr9)
print("Data type of the array:", arr9.dtype)