#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    data = np.loadtxt('../data/clustered_points_multicluster.txt',  delimiter=' ')
    x1 = data[:, 0]
    y1 = data[:, 1]

    arr_size_x = x1.size
    arr_size_y = y1.size

    print(arr_size_x)

    cluster_set = set([0])

    for index in range(arr_size_x):
        cluster_set.add(data[index,2])
    
    cluster_size = len(cluster_set)

    print("cluster size = (%d)" %(cluster_size))

    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 

    x_mean = a_0.mean()
    y_mean = a_1.mean()

    # a_0 = a_0 - x_mean
    # a_1 = a_1 - y_mean

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('robot pose error')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(a_0, a_1, s=2, c='g', marker='.')
    plt.xlim(xmax = x_mean+1, xmin=x_mean-1.)
    plt.ylim(ymax = y_mean+1., ymin=y_mean-1.)
#    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    draw_scatter()
