#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    # data = np.loadtxt('/home/lyb/projects/amcl_voxel_filter/voxel_filter/build/filtered_points.txt',  delimiter=' ')
    data = np.loadtxt('/home/lyb/tools_ws/src/test_tools/record_data/scan_error.txt',  delimiter=' ')
    x1 = data[:, 1]
    y1 = arange(x1.size())
    
    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 

    # a_0 = a_0 - x_mean
    # a_1 = a_1 - y_mean

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('filtered points')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(a_1, a_0, s=2, c='g', marker='.')
    # plt.xlim(xmax = x_mean+1, xmin=x_mean-1.)
    # plt.ylim(ymax = y_mean+1., ymin=y_mean-1.)

    plt.xlim(xmax = 0.2, xmin= -0.2)
    plt.ylim(ymax = 0.2, ymin= -0.2)
#    plt.gca().set_aspect('equal', adjustable='box')
    # plt.savefig( 'cluster_particlecloud.png') 
    plt.show()

if __name__ == "__main__":
    draw_scatter()
