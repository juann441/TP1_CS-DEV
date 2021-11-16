#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:51:43 2021

@author: juan.reyes-ortiz
"""

def mesImpots(revenu):
    impots=0
    if revenu <=10084:
        impots+=0
    if 10085<=revenu<=25710:
        impots+=(0.11)*(revenu-10085)
    if 25711<=revenu<=73516:
        impots+=(0.30)*(revenu-25711)+(0.11)*(25710-10085)
    if 73517<=revenu<=158122:
        impots+=(0.41)*(revenu-73517)+(0.11)*(25710-10085)+(0.3)*(73516-25711)
    if 158123<=revenu:
        impots+=(0.45)*(revenu-158123)+(0.11)*(25710-10085)+(0.3)*(73516-25711)+(0.41)*(158122-73517)
    return (impots)



def principal ():
    m_rev=input("montant des revenus: ")
    rev=int(m_rev)
    Impots=mesImpots(rev)
    return Impots
    
        