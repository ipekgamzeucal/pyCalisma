#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:28:11 2019

@author: ipekgamzeucal
"""

birler={"0":"","1":"bir","2":"iki","3":"üç","4":"dört","5":"beş","6":"altı","7":"yedi","8":"sekiz","9":"dokuz"}
onlar={"1":"on","2":"yirmi","3":"otuz","4":"kırk","5":"elli","6":"altmış","7":"yetmiş","8":"seksen","9":"doksan"}

def oku(sayı):
    onlarText=onlar.get(sayı[0])
    birlerText=birler.get(sayı[1])
    sayıText=onlarText+" "+birlerText
    return sayıText

sayı=input("Bana 2 basamaklı bir sayı söyle, sana okuyayım...")
if len(sayı)!=2 or sayı[0]=="0":
    print("Sayı 2 basamaklı değil, beni kandırma...")
else:
    print(oku(sayı))