#kurva berbentuk lonceng yang didirikan oleh mean daan deviansi standar

import numpy as np
import matplotlib.pyplot as plt

normal_data = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(normal_data, bins=30, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()