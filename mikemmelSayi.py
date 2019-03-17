#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:51:13 2019

@author: ipekgamzeucal
"""

print("""
      ********************
      
      Mikemmel Sayı Bulmaca
      
      ********************
      """)

sayi = int(input("Gir bi sayı, mikemmel mi bakalım:"))


bolenler=0

for x in range(1,sayi):
    kalan=sayi%x
    if kalan==0:
        bolenler+=x

if bolenler==sayi:
    print("Mikemmel sayi!")
else:
    print("Bu sayıdan bişi olmaz dostum...")