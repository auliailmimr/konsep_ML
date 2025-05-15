import numpy as np

G = np.array([[2,0],
             [0,3]])

eigenvalues=np.linalg.eigvals(G)
print(eigenvalues)