#!/usr/bin/python

from matplotlib import pyplot as plt

filename = 'amcl_pose.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

file1=[]
row=[]

for line in lines:
    row = line.split()
    file1.append(row)

data_x=[]
data_y=[]

for row1 in file1:
    data_x.append(row1[0])
    data_y.append(row1[1])


fig = plt.figure(figsize=(100,100))
ax1 = fig.add_subplot(111)
plt.xlim(-50,50)
plt.ylim(-50,50)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot(data_x, data_y, 'red')

plt.legend()
plt.show()
