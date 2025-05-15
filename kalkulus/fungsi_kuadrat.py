import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2 - 4*3 + 3

plt.plot(x, y, label ='f(x)=x**2 - 4*3 + 3')
plt.title('Quadratic Function')
plt.legend()
plt.show()