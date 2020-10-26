#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    # data = np.loadtxt('/home/lyb/projects/amcl_voxel_filter/voxel_filter/build/filtered_points.txt',  delimiter=' ')
    data = np.loadtxt('/home/lyb/cluster_particlecloud.txt',  delimiter=' ')
    x1 = data[:, 0]
    y1 = data[:, 1]
    
    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 

    x_mean = a_0.mean()
    y_mean = a_1.mean()

    # a_0 = a_0 - x_mean
    # a_1 = a_1 - y_mean

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('filtered points')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(a_0, a_1, s=2, c='g', marker='.')
    # plt.xlim(xmax = x_mean+1, xmin=x_mean-1.)
    # plt.ylim(ymax = y_mean+1., ymin=y_mean-1.)

    plt.xlim(xmax = x_mean+0.2, xmin=x_mean-0.2)
    plt.ylim(ymax = y_mean+0.2, ymin=y_mean-0.2)
#    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig( 'cluster_particlecloud.png') 
    plt.show()

if __name__ == "__main__":
    draw_scatter()
