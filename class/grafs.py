import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib import colors
import scipy.stats


class Paintgraf:

    def show_line(self, data, data2):
        plt.plot(data, data2)
        plt.xlabel('entry a')
        plt.ylabel('entry b')
        plt.grid(True)
        plt.show()

    def show_group(self, data, data2):
        names = ['0', '1']
        values = [data, data2]
        plt.figure(1, figsize=(5, 5))
        plt.bar(names, values)
        plt.grid(True)
        plt.show()

    def show_hist(self, data, mu, sigma):
        num_bins = 30
        n, bins, patches = plt.hist(data, num_bins, density=2, facecolor='green', alpha=0.5)
        y = scipy.stats.norm.pdf(bins, mu, sigma)
        plt.plot(bins, y, 'r--')
        plt.xlabel('Значение')
        plt.ylabel('Вероятность')
        plt.subplots_adjust(left=0.15)
        plt.show()

    def show_importances(self, importances, indices, names_indices):
        plt.figure()
        plt.title("Важность параметра")

        plt.bar(range(len(importances)), importances[indices], color="g")
        plt.xticks(range(len(importances)), names_indices, rotation=90)

        plt.tight_layout()
        plt.xlim([-1, len(importances)])
        plt.show()