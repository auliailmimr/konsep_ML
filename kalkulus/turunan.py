import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*3**3 - 6*x**2 + x - 4

def first_derivative(x):
    return 9*x**2 - 12*x + 1

def second_derivative(x):
    return 18*x - 12

x = np.linspace(-2, 4, 400)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, first_derivative(x), label="f'(x)")
plt.plot(x, second_derivative(x), label="f''(x)")
plt.title("Derivatives of a Polinomial Function")
plt.legend()
plt.show()
