#semua hasil memiliki kemungkinan yang sama

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
uniform_data=np.random.uniform(0,1,1000)
plt.hist(uniform_data, bins=30, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


