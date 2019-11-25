#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:13:07 2019

@author: toby
"""

import numpy as np
xy=np.loadtxt('xy-coordinates.dat')
#comment lines are stipped out
print(xy)
print(xy[0,1])#first row, second column
print(xy[:,0])#whole of first column
xy[:,1]+=2.5#add 2.5 to each element in second column
#print(xy)
#write it back out cleanly
args = {
        'header':'XY coords',
        'fmt':'%7.3f',
        'delimiter':','
        }
#np.savetxt('output.dat',xy,**args)