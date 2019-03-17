#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:47:54 2019

@author: ipekgamzeucal

list comprehension kullanarak 1'den 100'e kadar olan sayılardan 
sadece çift sayıları bir listeye atmayı yapmayı çalışın.
"""
theOnes=[x for x in range(1,101) if x%2==0]
print(theOnes)