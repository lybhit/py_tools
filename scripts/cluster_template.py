import numpy as np
from numpy import *
from operator import *
import matplotlib.pyplot as plt

def filemattrix(filename):                   
    fr = open(filename)
    arrayLines = fr.readlines()
    numberLines = len(arrayLines)
    returnMat = zeros((numberLines,2))
    labels = []
    index = 0
    for line in arrayLines:
        line = line.strip()
        listLine = line.split(' ')
 
        returnMat[index,:] = listLine[0:2]
        labels.append(int(listLine[-1]))
        index +=1
    return returnMat,labels

# returnMat, labels = filemattrix('../data/clustered_points_600_index.txt')
returnMat, labels = filemattrix('/home/lyb/cluster_particlecloud.txt')
 
fig = plt.figure()
axes = fig.add_subplot(111)
 
for i in range(len(labels)):
    if labels[i] ==0:
        axes.scatter(returnMat[i:i+1, 0], returnMat[i:i+1 ,1],color = 'red')
    if labels[i] == 1:
        axes.scatter(returnMat[i:i+1, 0], returnMat[i:i+1, 1], color='green')
 
    if labels[i] == 2:
        axes.scatter(returnMat[i:i+1, 0], returnMat[i:i+1, 1], color='black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cluster Chart')
plt.show()