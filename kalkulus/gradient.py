import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 4*x + 3

def df_dx(x):
    return 2*x - 4

def gradient_descent(init_x, learning_rate=0.1, iterations=10):
    x=init_x
    x_history = [x]
    for _ in range(iterations):
        grad = df_dx(x)
        x-=learning_rate*grad
        x_history.append(x)
    return x, x_history

x_min, x_history = gradient_descent(0.0)
x=np.linspace(-2, 4, 400)
y=f(x)

plt.plot(x, y, 'r-', label='f(x)=x^2 - 4x + 3')
plt.plot(x_history, f(np.array(x_history)),'bo',label='Gradient Descent', markersize=3 )
plt.title("Gradient Descent Visualization")
plt.legend()
plt.show()
