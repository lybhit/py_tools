#!/bin/bash python

import sys

path = "/home/syy001/test_data/amcl_pose_cov_a_82020-12-11T06:26:20.764911.txt" 
f = open(path)
line = f.readline()
list = []
while line:
    a = line.split(' ')
    b = a[1:] 
    list.append(b)
    line = f.readline()
f.close()

#print(list)

with open('/home/syy001/test_data/amcl_1211.txt', 'a') as month_file:  
    for line in list:
        s = ' '.join(line)
        month_file.write(s)
