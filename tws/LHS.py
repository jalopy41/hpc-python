#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:50:52 2019

@author: toby
"""

import numpy as np
import matplotlib.pyplot as plt
def latin_hypercube_2d(n):
    lower_limits=np.arange(0,n)/n
    upper_limits=np.arange(1,n+1)/n
    #uniformly distributed - any number is equally likely to be drawn
    points=np.random.uniform(low=lower_limits,high=upper_limits, size=[2,n]).T
    np.random.shuffle(points[:,1])
    
    return points

n=25
p=latin_hypercube_2d(n)
print(p)
plt.figure(figsize=[5,5])
plt.xlim([0,1])
plt.ylim([0,1])
plt.scatter(p[:,0],p[:,1],c='green')

for i in np.arange(0,1,1/n):
    plt.axvline(i)
    plt.axhline(i)

plt.show()