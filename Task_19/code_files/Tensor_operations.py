# -*- coding: utf-8 -*-
"""Tensor_Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtwXkoTL7FmPsff5qJwe2WjtxzaMbWJv
"""

import numpy as np

a = np.array([[11, 2], [13, 4]])
b = np.array([[15, 6], [17, 8]])

c = np.add(a, b)
d = np.subtract(a, b)
e = np.multiply(a, b)
f = np.divide(a, b)

print("Addition\n",c)
print("Subtraction\n",d)
print("Multiplication\n",e)
print("Division\n",f)