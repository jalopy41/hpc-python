#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:05:03 2019

@author: toby
"""

import numpy as np
import numexpr
import time


#a=np.arange(100)
#b=a[:]+3
#print(a,'\n',b)
a=776.0
t0 = time.process_time()
numexpr.set_num_threads(1)
poly=numexpr.evaluate("((.25*a+.75)*x -1.5)*x-2*sin(x)")
t1 = time.process_time()
print("one thread: ", t1 - t0)
t0 = time.process_time()
numexpr.set_num_threads(2)
poly=numexpr.evaluate("((.25*a+.75)*x -1.5)*x-2*sin(x)")
t1 = time.process_time()
print("two threads: ", t1 - t0)
t0 = time.process_time()
numexpr.set_num_threads(4)
poly=numexpr.evaluate("((.25*a+.75)*x -1.5)*x-2*sin(x)")
t1 = time.process_time()
print("four threads: ", t1 - t0)
numexpr.set_num_threads(8)
poly=numexpr.evaluate("((.25*a+.75)*x -1.5)*x-2*sin(x)")
t1 = time.process_time()
print("eight threads: ", t1 - t0)
a = np.zeros((4, 8))
print(a,'\n')
a[2, :] = np.arange(8)
print(a,'\n')
print(a[2:, 6:],'\n')  #2nd row onwards, last 2 elements in cols
#or, equivalently, 
print(a[-2:, -2:],'\n')  #last 2 rows, last 2 cols
print(a[2, 6],'\n')  
print(a[2:, -2:].ravel())