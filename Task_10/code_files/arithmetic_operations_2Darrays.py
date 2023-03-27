import numpy as np

A = np.array([[11, 21], [3, 4]])
B = np.array([[51, 6], [71, 8]])

print("Addition")
C = A + B
print(C)
print("-----------------------")

print("Subtraction")
C = A - B
print(C)
print("-----------------------")

print("Multiplication")
C = A * B
print(C)
print("-----------------------")

print("Matrix multiplication")
C = np.dot(A, B)
print(C)
print("-----------------------")

print("Division")
C = A / B
print(C)
