import numpy as np

#  numpy array
arr1 = np.array([111, 20, 3, 4, 5])
print("Numpy array:", arr1)
print("-----------------------------")

# Accessing elements of the numpy array
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Elements from 2nd to 4th:", arr1[1:4])
print("-----------------------------")

# Shape and size of the numpy array
print("Shape of array:", arr1.shape)
print("Size of array:", arr1.size)
print("-----------------------------")

# Reshaping the numpy array
arr_reshape = arr1.reshape(5, 1)
print("Reshaped array:\n", arr_reshape)
print("-----------------------------")

# 2D numpy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Numpy array:\n", arr_2d)
print("-----------------------------")

# Accessing elements of 2D numpy array
print("Element at row 1, column 2:", arr_2d[0][1])
print("Elements from 1st row:", arr_2d[0, :])
print("Elements from 2nd column:", arr_2d[:, 1])
print("-----------------------------")

# numpy array with zeros
arr_zeros = np.zeros((2, 3))
print("Numpy array with zeros:\n", arr_zeros)
print("-----------------------------")

#  numpy array with ones
arr_ones = np.ones((3, 4))
print("Numpy array with ones:\n", arr_ones)
print("-----------------------------")

# Creating a numpy array with random values
arr_random = np.random.rand(2, 3)
print("Numpy array with random values:\n", arr_random)
