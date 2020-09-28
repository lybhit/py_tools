#!/usr/bin/python

from matplotlib import pyplot as plt
import math
import numpy as np

#filename = 'compare_pose.txt'
filename = 'robot_pose.txt'

# data_x=[]
# data_y=[]

# data_1_x=[]
# data_1_y=[]

# delta_x=[]
# delta_y=[]

# with open(filename, 'r') as f:
#     for lines in f.readlines():
#         data_x.append(np.float64(lines.split(' ')[0]))
#         data_y.append(np.float64(lines.split(' ')[1]))
#         data_1_x.append(np.float64(lines.split(' ')[3]))
#         data_1_y.append(np.float64(lines.split(' ')[4]))
#         delta_x.append(np.float64(lines.split(' ')[0]) - float(lines.split(' ')[3]))
#         delta_y.append(np.float64(lines.split(' ')[1]) - float(lines.split(' ')[4]))

index=[]
trans=[]

data = np.loadtxt('robot_pose.txt',  delimiter=',')

data_x = data[:, 0]
data_y = data[:, 1]

data_1_x = data[:, 3]
data_1_y = data[:, 4]

delta_x = data_x - data_1_x
delta_y = data_y - data_1_y

j=0
index_j=[]
for x in delta_x:
    index_j.append(j)
    j = j+1

k=0
index_k=[]
for y in delta_y:
    index_k.append(k)
    k=k+1

i = 0
total_sum=0
for x in delta_x:
    trans.append(math.sqrt(pow(delta_x[i],2) + pow(delta_y[i],2)))
    total_sum=total_sum+math.sqrt(pow(delta_x[i],2) + pow(delta_y[i],2))
    index.append(i)
    i = i+1
    
mean = total_sum / i 

print(mean)


# fig = plt.figure(figsize=(100,100))
# ax1 = fig.add_subplot(111)
# plt.xlim(-50,50)
# plt.ylim(-50,50)
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.plot(data_x, data_y, 'red')

plt.plot(data_x, data_y, color = 'r', label = 'real')
plt.plot(data_1_x, data_1_y, color = 'b', label = 'optimal')

#plt.plot(index, trans, color = 'r', label = 'real')
#plt.plot(index_j, delta_x, color = 'r', label = 'real')
#plt.plot(index_k, delta_y, color = 'r', label = 'real')

plt.legend(loc='best')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
