#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:01:55 2019

@author: ipekgamzeucal
"""

print("""
      ********************
      
      Armstrong Sayısı Bulmaca
      
      ********************
      """)

sayi = input("Gir bi sayı, Armstrong mu bakalım:")

kuvvet=len(sayi)

toplam=0
for x in range(0,kuvvet):
    deger=int(sayi[x]) ** kuvvet
    toplam+=deger
    
if int(sayi)==toplam:
    print("Armstrong sayısı!")
else:
    print("Bu sayıdan Armstrong olmaz dostum...")

