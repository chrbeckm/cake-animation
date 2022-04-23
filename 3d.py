from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation, PillowWriter

d3 = np.genfromtxt("data/3d.csv", delimiter=",", missing_values="")

d30, d31 = d3.shape

x = np.outer(np.arange(d30), np.ones(d30))
y = np.outer(np.arange(d31), np.ones(d31)).T

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(x, y, d3, cmap=cm.Blues)
ax.set_xlim(0, d30 - 1)
ax.set_ylim(0, d31 - 1)

plt.plot(x[d3 == 6], y[d3 == 6], d3[d3 == 6], "y*", markersize=10)
ax.set_xticks([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_zticks([])
ax.set_zticklabels([])

frameInFig = ax.text(1, 1, 5, "0")

year = 24


def rotate(angle):
    ax.view_init(30, angle / (year + 1) * 360)
    frameInFig.set_text(angle)
    return [ax]


anim = FuncAnimation(fig, func=rotate, frames=np.arange(0, year + 1))
anim.save("build/3d.gif", writer="Pillow")
