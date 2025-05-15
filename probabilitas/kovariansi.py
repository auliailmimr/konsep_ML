#mengukur tingkat ketergantungan linear antara dua variabel acak

import numpy as np

np.random.seed(0)
X=np.random.normal(loc=0, scale=1, size=1000)
Y=np.random.normal(loc=0, scale=1, size=1000)

covariance_matrix=np.cov(X, Y)
covariance=covariance_matrix[0,1]
print(f"Covariance matriksnya adalah : {covariance}")