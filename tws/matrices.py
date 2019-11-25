#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:45:03 2019

@author: toby
"""

import numpy as np
import matplotlib.pyplot as plt
A=np.array(((2,1),(1,3)))
B=np.array(((-2,4.2),(4.2,6)))
C=np.dot(A,B)

b=np.array((1,2))

print(C,'\n',b)
print('solving Cx = b')
x=np.linalg.solve(C,b)
print(x)

#----Eigenvalues----
#construct 2 symmetric matrices
Asym=A+np.transpose(A)
B=np.array(((4,3),(2,-1)))
Bsym=B+np.transpose(B)
print(Asym,'\n',Bsym)
C=np.dot(A,B)
Eig=np.linalg.eigvals(C)
print('Eigenvals:',Eig)
#----Polynomials----
x = np.linspace(0, 8, 15)
f = x**2 + np.random.random(x.shape)
p = np.polyfit(x, f, 2)
#print(p)
#print(p[0])
y=np.zeros(7,float)
y = x**p[0]+x*p[1]+p[2]
#print(y)
#plt.plot(x,y,'r')
#plt.scatter(x,f)
#plt.show()