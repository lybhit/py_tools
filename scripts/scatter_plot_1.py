#!/usr/bin/python
#-*- coding: UTF-8 -*- 

import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

filename = 'amcl_pose.txt'
#filename = 'amcl_pose_whole.txt'

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

colors1 = '#00CED1'
area = 0.5
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=100,xmin=-100)
plt.ylim(ymax=100,ymin=-100)
#plt.scatter(data_x, data_y, s=area, c="#ff1212", marker='o')
plt.scatter(data_x, data_y, s=area, c="#00CED1", marker='o')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
#plt.savefig(r'./data.png', dpi=300)
plt.show()
