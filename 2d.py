import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

np.set_printoptions(linewidth=150)

d2_bw = np.genfromtxt("data/2d_bw.csv", delimiter=";")

plt.figure(constrained_layout=True)
ax = plt.axes()
for name in ["bottom", "left", "top", "right"]:
    ax.spines[name].set_color("white")
plt.imshow(d2_bw, cmap="binary", aspect=0.8, vmin=0, vmax=1)
plt.xticks([], [])
plt.yticks([], [])
plt.savefig("build/2d_bw.png")
plt.clf()

d2_color = np.genfromtxt("data/2d_color.csv", delimiter=";", missing_values="")

plt.figure(constrained_layout=True)
ax = plt.axes()
for name in ["bottom", "left", "top", "right"]:
    ax.spines[name].set_color("white")
plt.imshow(d2_color, cmap="Paired", aspect=0.8, vmin=0, vmax=11)
plt.xticks([], [])
plt.yticks([], [])
plt.savefig("build/2d_color.png")
plt.clf()

nrOfLines = d2_color.shape[0]
empty = np.full(d2_color.shape, np.nan)
empty2 = np.full(d2_color.shape, np.nan)
empty3 = np.full(d2_color.shape, np.nan)
empty4 = np.full(d2_color.shape, np.nan)
empty5 = np.full(d2_color.shape, np.nan)
empty_row = np.zeros(len(d2_color[0]))

fig = plt.figure(constrained_layout=True)
ax = plt.subplot(111)

for name in ["bottom", "left", "top", "right"]:
    ax.spines[name].set_color("white")


def anim_func(i):
    print(f"Frame: {i}/{4 * nrOfLines}")
    if i < nrOfLines:
        empty[i, :] = d2_bw[i, :]
        ax.imshow(empty, cmap="binary", aspect=0.8, vmin=0, vmax=1)
    elif i >= nrOfLines and i < 2 * nrOfLines:
        i -= nrOfLines - 1
        empty2[-i, :] = d2_color[-i, :]
        ax.imshow(empty2, cmap="Paired", aspect=0.8, vmin=0, vmax=11)
    elif i >= 2 * nrOfLines - 1 and i < 3 * nrOfLines:
        i -= 2 * nrOfLines
        empty5[i, :] = empty_row
        ax.imshow(empty5, cmap="binary", aspect=0.8, vmin=0, vmax=1)
        empty3[i, :] = d2_bw[i, :]
        ax.imshow(empty3, cmap="binary", aspect=0.8, vmin=0, vmax=1)
    else:
        i -= 3 * nrOfLines
        empty4[-i, :] = empty_row
        ax.imshow(empty4, cmap="binary", aspect=0.8, vmin=0, vmax=1)
    return (ax,)


plt.xticks([], [])
plt.yticks([], [])
anim = FuncAnimation(fig, anim_func, frames=np.arange(4 * nrOfLines))

anim.save("build/2d.gif", writer="Pillow")
