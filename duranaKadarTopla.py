#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:33:51 2019

@author: ipekgamzeucal
"""
toplam=0
while True:
    sayi=input("Topluyorum, bana dur demek için 'q'ya bas.Güncel Toplam:{} Sayı:".format(toplam))
    if sayi!="q":
        toplam+=int(sayi)
    elif sayi=="q":
        print("Siiii Yaaaa ! Yine gel..")
        break
    
    