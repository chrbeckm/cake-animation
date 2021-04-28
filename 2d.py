import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

d2_bw = np.genfromtxt('data/2d_bw.csv', delimiter=';')

plt.figure(constrained_layout=True)
ax = plt.axes()
for name in ['bottom', 'left', 'top', 'right']:
    ax.spines[name].set_color('white')
plt.imshow(d2_bw, cmap='binary', aspect=.8, vmin=0, vmax=1)
plt.xticks([],[])
plt.yticks([],[])
plt.savefig('build/2d_bw.png')
plt.clf()

d2_color = np.genfromtxt('data/2d_color.csv', delimiter=';', missing_values='')

plt.figure(constrained_layout=True)
ax = plt.axes()
for name in ['bottom', 'left', 'top', 'right']:
    ax.spines[name].set_color('white')
plt.imshow(d2_color, cmap='Paired', aspect=.8, vmin=0, vmax=11)
plt.xticks([],[])
plt.yticks([],[])
plt.savefig('build/2d_color.png')
plt.clf()

nrOfLines = d2_color.shape[0]
empty = np.full(d2_color.shape, np.nan)
empty2 = np.full(d2_color.shape, np.nan)

fig = plt.figure(constrained_layout=True)
ax = plt.subplot(111)

for name in ['bottom', 'left', 'top', 'right']:
    ax.spines[name].set_color('white')

def anim_func(i):
    if i < nrOfLines:
        empty[i,:] = d2_bw[i,:]
        ax.imshow(empty, cmap='binary', aspect=.8, vmin=0, vmax=1)
    else:
        i -= nrOfLines - 1
        empty2[-i,:] = d2_color[-i,:]
        ax.imshow(empty2, cmap='Paired', aspect=.8, vmin=0, vmax=11)
    return ax,

plt.xticks([],[])
plt.yticks([],[])
anim = FuncAnimation(fig, anim_func, frames=np.arange(2 * nrOfLines))

anim.save('build/2d.gif', writer='Pillow')
