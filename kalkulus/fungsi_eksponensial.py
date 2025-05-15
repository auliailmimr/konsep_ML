import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,400)
y=2**x

plt.plot(x, y, label='f(x)=2^x')
plt.title("Eksponensial Function")
plt.legend()
plt.show()