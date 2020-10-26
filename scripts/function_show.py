import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
fig = plt.figure(1)
ax = fig.add_subplot(1,1,1) 
 
t = np.linspace(0, 1, 200)
#theta = t * 2 * np.pi
 
# r(t)=(sint,cost,t)
x = t
y = t
ax.plot(x, y, label='r(t)')
 
x = t
y = t*t
ax.plot(x, y, label='r(t*t)')
 
x = t
y = t*t*t
ax.plot(x, y, label='r(t*t*t)')

ax.legend()
plt.show()