import numpy as np
import matplotlib.pyplot as plt

exponential_data = np.random.exponential(scale=1, size=1000)
plt.hist(exponential_data, bins=30, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
