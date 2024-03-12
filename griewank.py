import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 

def gradient(x, y):
  grad_x = (x / 2000) + (np.sin(x / np.sqrt(1)) / np.sqrt(1))
  grad_y = (y / 2000) + (np.sin(y / np.sqrt(1)) / np.sqrt(1))
  return grad_x, grad_y


def targetFunction(x, y):
  return (x**2/4000 - np.cos(x/np.sqrt(1))) + (y**2/4000 - np.cos(y/np.sqrt(1))) + 1


def gradientDescent(targetFunction, x0, y0, step_size, tolerance):
  x = x0
  y = y0
  n = 0
  value = targetFunction(x0, y0)

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
    
    if (n%5 == 0):
      ax.scatter(x, y, targetFunction(x, y), c='red', s=10)

  return x_min, y_min


x0 = 2
y0 = 2
step_size = 0.1
tolerance = 1e-5
max_steps = 3000

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x, y = np.meshgrid(x, y)
z = (x**2/4000 - np.cos(x/np.sqrt(1))) + (y**2/4000 - np.cos(y/np.sqrt(1))) + 1
fig = plt.figure()

ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, alpha=0.3, rstride=1, cstride=1, cmap=cm.nipy_spectral, linewidth=0.08,
  antialiased=True)

x_min, y_min  = gradientDescent(targetFunction, x0, y0, step_size, tolerance)

print("Minimum dla:" , x_min, y_min)  
print("Wartość w minimum:", targetFunction(x_min, y_min))

plt.show() 