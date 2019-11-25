#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:22:22 2019

@author: toby
"""
import numpy as np
import matplotlib.pyplot as plt
a=np.random.random((2,2))
print(a)

b=np.random.choice(np.arange(8),10)#choose 8 nos from range 0-9
print(b)

a=np.random.random(size=1000)
mean=np.mean(a)
print(mean)
stdev=np.std(a)
print(stdev)
plt.hist(a,50)
plt.show()

a=np.random.normal(size=1000)
mean=np.mean(a)
print(mean)
stdev=np.std(a)
print(stdev)
plt.hist(a,50)
plt.show()