import numpy as np
from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import example_functions

# Use marching cubes to plot implicit surface
xl = np.linspace(-3, 3, 50)
X, Y, Z = np.meshgrid(xl, xl, xl)
F = example_functions.goursat_tangle(X, Y, Z)

verts, faces, normals, values = measure.marching_cubes(
    F, 0, spacing=[np.diff(xl)[0]] * 3
)
verts -= 3
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_trisurf(verts[:, 1], verts[:, 0], faces, verts[:, 2], cmap="jet", lw=0)

plt.show()
