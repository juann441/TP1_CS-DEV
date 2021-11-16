#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:01:53 2021

@author: juan.reyes-ortiz
"""


        
def hanoi(n,a=1,b=2,c=3,d=0):
    if (n > 0):
        hanoi(n-1,a,c,b)
        print ("Déplacer le disque du plot ",a,"vers le plot",c)
        hanoi(n-1,b,a,c)