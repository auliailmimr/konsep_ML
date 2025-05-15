import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.1, 10, 400)
y=np.log(x)

plt.plot(x, y, label='f(x)=log(x)')
plt.title("Logarithmic Function")
plt.legend()
plt.show()