import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
from collections import OrderedDict

d3 = np.genfromtxt('data/3d.csv', delimiter=',', missing_values='')

d30, d31 = d3.shape

x = np.outer(np.arange(d30), np.ones(d30))
y = np.outer(np.arange(d31), np.ones(d31)).T


def plot_color_gradients(cmap_category, cmap_list):
    for name in cmap_list:
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.plot_surface(x, y, d3, cmap=plt.get_cmap(name))
        ax.set_xlim(0, d30-1)
        ax.set_ylim(0, d31-1)
        plt.plot(x[d3==6], y[d3==6], d3[d3==6], 'y*', markersize=10)
        ax.set_xticks([])
        ax.set_xticklabels([])
        ax.set_yticks([])
        ax.set_yticklabels([])
        ax.set_zticks([])
        ax.set_zticklabels([])
        plt.savefig(f'build/3d-{cmap_category}-{name}.png')


cmaps = OrderedDict()
cmaps['Perceptually Uniform Sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']
cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
cmaps['Sequential (2)'] = [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']
cmaps['Diverging'] = [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']
cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']
cmaps['Miscellaneous'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
            'gist_ncar']

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list)
