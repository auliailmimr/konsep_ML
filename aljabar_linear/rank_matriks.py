import numpy as np

E = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
rank_E = np.linalg.matrix_rank(E)
print(rank_E)