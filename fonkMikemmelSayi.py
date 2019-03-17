#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:00:06 2019

@author: ipekgamzeucal
"""

print("""
      ********************
      
      Fonksiyon ile Mikemmel Sayı Bulmaca
      
      ********************
      """)

def mikemmelSayi(sayi):
    bolenler=0
    for x in range(1,sayi):
        if sayi%x ==0:
            bolenler+=x
    return bolenler==sayi     

for i in range(1,1001):
    if(mikemmelSayi(i)):
        print("Mikemmel Sayı!", i)
