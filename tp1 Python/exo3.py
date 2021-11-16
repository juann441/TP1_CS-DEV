#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:31:41 2021

@author: juan.reyes-ortiz
"""

def multiplication():

    x = [[12,7,3],
         [12 ,5,6],
         [7 ,8,9]]
    y = [[5,5,1],
         [6,7,3],
         [4,5,9]]
    
    res = [[0,0,0],
           [0,0,0],
           [0,0,0]]
    
    
    for i in range(len(x)):
       for j in range(len(y[0])):
        for k in range(len(y)):
            res[i][j] += x[i][k] * y[k][j]
    
    for r in res:
       print(r)

    
    
        