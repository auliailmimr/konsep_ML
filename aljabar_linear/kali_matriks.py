import numpy as np

A = np.array([[2,3,4],
              [5,6,7]])
B = np.array([[1,2],
              [3, 4],
              [5, 6]])
C = np.dot(A,B)
print(C)