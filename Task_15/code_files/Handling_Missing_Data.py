# Handling Missing Data
print("Handling Missing Data")
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, 3, None, 4],
                   'B': [None, 6, 67, 8],
                   'C': [9, 99, 11, None]})
print(df)
print("---------------------------------------")

Null_values = df.isnull()
print(Null_values)
print("---------------------------------------")

# fill missing values with a constant value
df.fillna(0, inplace=True)
print(df)
print("---------------------------------------")

# drop rows with missing values
df.dropna(axis=0, inplace=True)
print(df)
print("---------------------------------------")

# drop columns with missing values
df.dropna(axis=1, inplace=True)
print(df)
print("======================================")



# Filling and Replacing Values

print("Filling and Replacing Values")

# replace specific values
df.replace({1: 100, None: 0}, inplace=True)
print(df)
print("---------------------------------------")

# fill missing values using forward fill
df.fillna(method='ffill', inplace=True)
print(df)
print("---------------------------------------")

# fill missing values using backward fill
df.fillna(method='bfill', inplace=True)
print(df)
print("=====================================")


# Removing Duplicates
print("Removing Duplicates")
# dataframe with duplicates
df1 = pd.DataFrame({'A': [11, 2, 2, 14],
                   'B': [5, 6, 6, 13],
                   'C': [9, 10, 10, 12]})
print(df1)
print("---------------------------------------")
df1.drop_duplicates(subset=['A', 'B'], inplace=True)
df1.drop_duplicates(keep='first', inplace=True)
df1.drop_duplicates(keep='last', inplace=True)
print(df1)
print("========================================")

# Detecting and Removing Outliers
print("Detecting and Removing Outliers")
df2 = pd.DataFrame({'A': [1, 12, 13, 4, 5, 100],
                   'B': [5, 6, 7, 18, 9, 100],
                   'C': [9, 10, 11, 12, 13, 100]})
print(df2)
print("---------------------------------------")

#  Z-score for each data point
z_scores = np.abs((df2 - df2.mean()) / df2.std())
print(z_scores)
print("---------------------------------------")
threshold = 3
outliers = z_scores > threshold

# remove outliers from the data
df2 = df2[~outliers.any(axis=1)]
print(df2)


