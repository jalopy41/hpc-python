import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
#output 2,3
#reshape to 3x2
a.shape=(3,2)
print(a)

#similarly, reshape() can be used
b=a.reshape(2,3)

#shorthand to flatten array to 1D
c=a.ravel()
print(c)
#equivalently...
a.reshape(a.size)

#Concatentate
a=([np.linspace(7,9,3)],[np.linspace(10,12,3)])
print(a)
a=np.array([[7,8,9],[10,11,12]])
print(a.shape,b.shape)
c=np.concatenate((b,a))
print(c)

#specific axis(dimension) to join
d=np.concatenate((b,a),axis=1)
print(d)

#splitting arrays
x=np.split(b,2)          #split into 2 1x3 arrays
y=np.split(b,3,axis=1)   #split into 3 2x1 arrays
print(x)
print(y)

#broadcasting
a=np.arange(4) #0,1,2,3
print(a*2)

#a 3x2 matrix multiplied by a 1x2 vector
a=np.arange(6).reshape(3,2)
b=np.array([7,11],float).reshape(1,2)
print(a,'\n',b,'\n\n',a*b)