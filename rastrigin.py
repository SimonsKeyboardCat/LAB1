import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from matplotlib.tri import Triangulation

def gradient(x, y):
  grad_x = 2 * x - 20 * np.pi * np.sin(2 * np.pi * x)
  grad_y = 2 * y - 20 * np.pi * np.sin(2 * np.pi * y)
  return grad_x, grad_y


def targetFunction(x, y):
  return (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)) + 20


def gradientDescent(targetFunction, x0, y0, step_size, tolerance):
  x = x0
  y = y0
  value = targetFunction(x0, y0)
  n = 0

  while True:
    grad_x, grad_y = gradient(x, y)
    x -= step_size * grad_x
    y -= step_size * grad_y
    n = n+1
    
    print(n, x, y, value)

    if (value > targetFunction(x, y)):
      x_min = x
      y_min = y
      value = targetFunction(x, y)

    if (np.sqrt(grad_x**2 + grad_y**2) < tolerance) or (n >= max_steps):
      break
    
    if (n%50 == 0):
      ax.scatter(x, y, targetFunction(x, y), c='red', s=10)

  return x_min, y_min


x0 = 2
y0 = 2
step_size = 0.01
tolerance = 1e-4
max_steps = 5000

x = np.linspace(-5.12, 5.12, 100)
y = np.linspace(-5.12, 5.12, 100)

x, y = np.meshgrid(x, y)
z = (x**2 - 10*np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y)) + 20
fig = plt.figure()

ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, alpha=0.1, rstride=1, cstride=1, cmap=cm.nipy_spectral, linewidth=0.08,
  antialiased=True)

x_min, y_min = gradientDescent(targetFunction, x0, y0, step_size, tolerance)

print("Minimum dla:" , x_min, y_min)  
print("Wartość w minimum:", targetFunction(x_min, y_min))

plt.show()  
  