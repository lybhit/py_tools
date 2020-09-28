#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    data = np.loadtxt('filtered_points_100.txt',  delimiter=' ')
    x1 = data[:, 0]
    y1 = data[:, 1]
    
    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('robot pose error')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(a_0, a_1, s=2, c='g', marker='.')
    plt.xlim(xmax = 30., xmin=-30.)
    plt.ylim(ymax = 10., ymin=-10.)
#    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    draw_scatter()
