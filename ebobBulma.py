#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:11:46 2019

@author: ipekgamzeucal
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)): #sayı1%i=0 ise not(sayı1%i)=True
                                                   #sayı1%i 0'dan farklıysa not(sayı1%i)=False
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))

"""

def ebobBul(x,y):
    
    ortakBolen=[]
    if x <= y:
        kucuk=x
    else:
        kucuk=y
    for i in range(2,kucuk+1):
        if x%i==0 and y%i==0:
            ortakBolen.append(i)
            ebob=max(ortakBolen)
    return ebob

print("Bana iki sayı söyle, sana eboblarını söyliyim...")
x=int(input("1.Sayı:"))
y=int(input("2.Sayı:"))
print("EBOB({},{})={}".format(x,y,ebobBul(x,y)))