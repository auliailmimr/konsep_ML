import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10, 10, 400)
y=np.sin(x)

plt.plot(x, y, label='f(x)=sin(x)')
plt.title('Trigonometric Function')
plt.legend()
plt.show()