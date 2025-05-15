import numpy as np

#Extracting vectors from a matrix
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
v_column = A[:,1]
print(v_column)

v_row = A[2,:]
print(v_row)

#Building a matrix from vectors
v1 = np.array([1,0,3])
v2 = np.array([0,1,4])
v3 = np.array([1,1,1])

M_as_row = np.array([v1,v2,v3])
print(M_as_row)

M_as_column = np.column_stack((v1, v2, v3))
print(M_as_column)

