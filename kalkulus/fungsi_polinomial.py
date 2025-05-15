import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,400)
y=0.1*x**3 - 0.5*x**2 + 2*x - 1

plt.plot(x, y, label='f(x)=0.1*x**3 - 0.5*x**2 + 2*x - 1')
plt.title("Polinomial Function")
plt.legend()
plt.show()