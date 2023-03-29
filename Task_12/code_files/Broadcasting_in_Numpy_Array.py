import numpy as np

# two arrays of different shapes
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([7, 8, 9])
print(arr1)
print("-" * 80)
print(arr2)
print("-" * 80)

# Adding the two arrays using broadcasting
print("Addition  using broadcasting")
result1 = arr1 + arr2
print(result1)

print("-" * 80)

#  subtraction
print("Subtraction  using broadcasting")
result2 = arr1 - arr2
print(result2)
print("-" * 80)

print("Mutiplication  using broadcasting")
result3 = arr1 * arr2
print(result3)
print("-" * 80)

print("Division using broadcasting")
result4 = arr1 / arr2
print(result4)