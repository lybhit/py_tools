#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def draw_scatter():
    data = np.loadtxt('robot_pose.txt',  delimiter=',')
    x1 = data[:, 0]
    y1 = data[:, 1]
    
    x2 = data[:, 3]
    y2 = data[:, 4]
    
    a_0 = np.asarray(x1) 
    a_1 = np.asarray(y1) 
    b_0 = np.asarray(x2) 
    b_1 = np.asarray(y2)

    c_0 = b_0 - a_0 
    c_1 = b_1 - a_1 
#    print(c_0)
    print("mean error on x axis") 
    print(c_0.mean())
    print("mean error on y axis") 
    print(c_1.mean())
#    print(c_0.var(), 2) 
#    print(c_1.var(), 2) 

    s_0 = pow(c_0, 2)
    s_1 = pow(c_1, 2)

    
    sum_err = np.sqrt(s_0 + s_1)
    print("mean error in Euclidean Distance")
    print(sum_err.mean())
    print(sum_err.var(), 1)    
    arr_var = np.var(s_0)
    arr_std = np.std(s_0, ddof=1)
#    print("---")
#    print(arr_var)
#    print(arr_std)
    n = s_0.size 
    n_row = np.size(s_0, 0)
#    print(n)

    nlist = np.linspace(1,n,num=n, dtype=np.int32)        
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('robot pose error')
    ax1.set_xlabel('x - value')
    ax1.set_ylabel('y - value')
    ax1.scatter(nlist, sum_err, s=2, c='g', marker='.')
    plt.xlim(xmax = n, xmin=0)
    plt.ylim(ymax = 0.2, ymin=0.0)
#    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    draw_scatter()
