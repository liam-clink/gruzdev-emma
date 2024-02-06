import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.tri import Triangulation

## Plot a sphere
# Parameters:
theta = np.linspace(0, 2 * np.pi, 20)
phi = np.linspace(0, np.pi, 20)
theta, phi = np.meshgrid(theta, phi)
rho = 1

# Parametrization:
x = np.ravel(rho * np.cos(theta) * np.sin(phi))
y = np.ravel(rho * np.sin(theta) * np.sin(phi))
z = np.ravel(rho * np.cos(phi))

# Triangulation:
tri = Triangulation(np.ravel(theta), np.ravel(phi))

# Render:
ax = plt.axes(projection="3d")
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap="jet", antialiased=True)
plt.show()
