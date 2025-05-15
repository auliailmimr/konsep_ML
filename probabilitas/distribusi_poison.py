import numpy as np
import matplotlib.pyplot as plt

poisson_data = np.random.poisson(lam=3, size=1000)
plt.hist(poisson_data, bins=30, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()