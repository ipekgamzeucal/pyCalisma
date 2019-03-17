#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:03:14 2019

@author: ipekgamzeucal
"""

def ekok(x,y):
    xKat=[]
    yKat=[]
    for i in range(1,x*y):
        xk=x*i
        yk=y*i
        xKat.append(xk)
        yKat.append(yk)
        if xk in yKat:
            ortakKat=xk
            break
    return ortakKat

print("Bana iki sayı söyle, sana ekoklarını söyliyim...")
x=int(input("1.Sayı:"))
y=int(input("2.Sayı:"))
print("EKOK({},{})={}".format(x,y,ekok(x,y)))
        