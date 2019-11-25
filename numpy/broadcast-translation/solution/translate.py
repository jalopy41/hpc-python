import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('points_circle.dat')
plt.plot(data[:,0], data[:,1], 'o')

vector = np.array((0.005, 0.05))
print(vector)
data_trans = data + vector
#plt.plot(data_trans[:,0], data_trans[:,1], 'd')

area = (30 * np.random.rand(50))**2
print(area)
plt.scatter(data_trans[:,0], data_trans[:,1], c='red',s=50,alpha=0.5)
plt.show()
