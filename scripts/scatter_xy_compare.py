#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    # data = np.loadtxt('/home/lyb/projects/amcl_voxel_filter/voxel_filter/build/filtered_points.txt',  delimiter=' ')
    data = np.loadtxt('/home/lyb/odom_filter_pose.txt',  delimiter=' ')
    x1 = data[:, 0]
    y1 = data[:, 1]

    data_2 = np.loadtxt('/home/lyb/amcl_pose_with_cov.txt',  delimiter=' ')
    x2 = data_2[:, 0]
    y2 = data_2[:, 1]

    # data_3 = np.loadtxt('/home/lyb/knn.txt',  delimiter=' ')
    # x3 = data_3[:, 0]
    # y3 = data_3[:, 1]
    
    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 

    b_0 = np.asarray(x2) 
    b_1 = np.asarray(y2) 

    # c_0 = np.asarray(x3) 
    # c_1 = np.asarray(y3) 

    x_mean = a_0.mean()
    y_mean = a_1.mean()

    # a_0 = a_0 - x_mean
    # a_1 = a_1 - y_mean

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('particle points')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(a_0, a_1, s=2, c='b', marker='.', label='filtered')
    ax1.scatter(b_0, b_1, s=1, c='r', marker='*', label='amcl_pose')
    # ax1.scatter(c_0, c_1, s=4, c='g', marker='*')
    # plt.xlim(xmax = x_mean+1, xmin=x_mean-1.)
    # plt.ylim(ymax = y_mean+1., ymin=y_mean-1.)

    plt.xlim(xmax = 100, xmin=-100)
    plt.ylim(ymax = 100, ymin=-100)
    # plt.gca().set_aspect(1)
    # plt.savefig( 'compare.png') 
    plt.legend()
    plt.show()

if __name__ == "__main__":
    draw_scatter()
