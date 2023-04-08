#  Combining and Merging Datasets
print("Combining")
import pandas as pd
import numpy as np

# Concatenating datasets vertically
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result1 = pd.concat([df1, df2])
print(result1)
print("------------------------------")
# Concatenating datasets horizontally

df3 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df4 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
result2 = pd.concat([df3, df4], axis=1)
print(result2)

print("===========================")

# Merging datasets based on common columns
print("Merging")
df5 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
df6 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': [5, 6, 7, 8]})
result3 = pd.merge(df5, df6, on='key')
print(result3)
print("===========================")

# Reshaping Data
print("Reshaping")
# Reshape with pandas
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
df7 = pd.DataFrame(data.reshape(2, 3))
print(df7)

# print("---------------------------")
# Reshaping Data with Numpy
data = np.array([1, 2, 3, 4, 5, 6])
reshaped = np.reshape(data, (2, 3))
print(reshaped)
print("-------------------------")
arr = np.array([[1, 2], [3, 4], [5, 6]])
transposed = np.transpose(arr)
print(transposed)

