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

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=100,xmin=-100)
plt.ylim(ymax=100,ymin=-100)
plt.scatter(data_x, data_y, s=area, c=colors1, alpha=0.4, label='类别A')
plt.legend()
#plt.savefig(r'./data.png', dpi=300)
plt.show()

