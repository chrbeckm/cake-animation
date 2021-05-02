import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import matplotlib.colors as col

d3 = np.genfromtxt('data/3d.csv', delimiter=',', missing_values='')

d30, d31 = d3.shape

x = np.outer(np.arange(d30), np.ones(d30))
y = np.outer(np.arange(d31), np.ones(d31)).T
colors = ["white", "brown", "red"]
nodes = [0.0, 0.53, 1]
cmap2 = col.LinearSegmentedColormap.from_list("mycmap", list(zip(nodes, colors)))

fig = plt.figure()
ax = mplot3d.Axes3D(fig)
ax.plot_surface(x, y, d3, cmap=cmap2)
ax.set_xlim(0, d30-1)
ax.set_ylim(0, d31-1)
plt.plot(x[d3==6], y[d3==6], d3[d3==6], 'y*', markersize=10)
ax.set_xticks([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_zticks([])
ax.set_zticklabels([])
plt.savefig('build/3d-own2.png')
