import numpy as np

# Mean of an array
print("Mean")
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
print(mean) 

# Mean of a matrix
mat = np.array([[1, 2], [3, 4], [5, 6]])
mean = np.mean(mat, axis=0)
print(mean) 
print("----------------------------")

# Median of an array
print("Median")
arr = np.array([1, 2, 3, 4, 5])
median = np.median(arr)
print(median) 

# Median of a matrix
mat = np.array([[1, 2], [3, 4], [5, 6]])
median = np.median(mat, axis=0)
print(median) 
print("----------------------------")

# # Mode of an array
print("Mode") 
def mode(arr):
    values, counts = np.unique(arr, return_counts=True)
    index = np.argmax(counts)
    return values[index]

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(mode(arr))
print("----------------------------")

# Quartiles of an array
print("Quartiles")
arr = np.array([1, 2, 3, 4, 5])
quartiles = np.percentile(arr, [25, 50, 75])
print(quartiles) 
print("----------------------------")

# Rank of a matrix
print("Rank")
mat = np.array([[1, 2], [3, 4], [5, 6]])
rank = np.linalg.matrix_rank(mat)
print(rank) 
print("----------------------------")

# Normal distribution
print("Normal distribution")
#  array of random numbers with a normal distribution
normal_dist = np.random.normal(loc=0, scale=1, size=10000)
# first 10 values
print(normal_dist[:4])
print("----------------------------")

# standard deviation 
print("Standard Deviation")
std_dev = np.std(arr)
print(std_dev)
print("------------------------------")

# correlation coefficient between two arrays
print("correlation coefficient between two arrays")
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
corr_coef = np.corrcoef(a, b)
print(corr_coef)
