#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:38:22 2021

@author: juan.reyes-ortiz
"""

def Syracuse(N):
   
    l_n=[N]
    while N!=1:
        if N%2==0:
            N=N//2
            l_n.append(N)
        else:
            N=(N*3)+1
            l_n.append(N)
    return l_n            
        