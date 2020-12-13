#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    # data = np.loadtxt('/home/lyb/projects/amcl_voxel_filter/voxel_filter/build/filtered_points.txt',  delimiter=' ')
    data = np.loadtxt('/home/syy001/test_data/amcl_1211.txt',  delimiter=' ')
    belief = data[:, 3]
    cov_x = data[:, 4]
    cov_y = data[:, 5]
    # cov_theta = data[:, 3]

    belief_arr = np.asarray(belief) 
    cov_x_arr = np.asarray(cov_x) 
    cov_y_arr = np.asarray(cov_y) 
    # cov_theta_arr = np.asarray(cov_theta) 

    a_size = belief_arr.size
    t = np.arange(0,0.02 * a_size, 0.02)

    print(t.size)
    
    print(a_size)

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('cov && belief')
    ax1.set_xlabel('t')
    ax1.set_ylabel('value')
    ax1.scatter(t, belief_arr, s=1, c='b', marker='.', label='bel')
    ax1.scatter(t, cov_x_arr, s=1, c='r', marker='.', label='cov')
    # ax1.scatter(c_0, c_1, s=4, c='g', marker='*')
    # plt.xlim(xmax = x_mean+1, xmin=x_mean-1.)
    # plt.ylim(ymax = y_mean+1., ymin=y_mean-1.)

    plt.xlim(xmax = 100, xmin=0)
    plt.ylim(ymax = 1, ymin=0)
    plt.legend()
    # plt.gca().set_aspect(1)
    # plt.savefig( 'cluster_particlecloud_1.png') 
    plt.show()

if __name__ == "__main__":
    draw_scatter()
