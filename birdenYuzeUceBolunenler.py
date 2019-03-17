#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:41:50 2019

@author: ipekgamzeucal
"""
theOnes=[]
for x in range(1,101):
    kalan=x%3
    if kalan==0:
        theOnes.append(x)
    else:
        continue
print(theOnes)