#menggambarkan jumlah keberhasilan dalam sejumlah percobaan yang independen

import matplotlib.pyplot as plt
import numpy as np

binomial_data=np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(binomial_data, bins=30, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()