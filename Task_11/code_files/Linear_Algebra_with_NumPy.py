import numpy as np

# 2x2 matrix
print("matrix")
A = np.array([[1, 2], [3, 4]])
print(A)
print("--------------------------")

# determinant of A
print("Determinant of matrix")
det = np.linalg.det(A)
print(det)
print("------------------------")

# inverse of A
print("Inverse of matrix")
inv = np.linalg.inv(A)
print(inv)
print("------------------------")

# eigenvalues and eigenvectors of A
print("Eiganvalues and Eigenvectoes of matrix")
eigvals, eigvecs = np.linalg.eig(A)
print("Eigan vales:", eigvals)
print("Eigan vectors:", eigvecs)
