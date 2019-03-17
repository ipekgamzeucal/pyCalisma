#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:12:19 2019

@author: ipekgamzeucal
"""

userAnswer=input("Hangi şeklin tipini belirlemek istersin.\n1-Dörtgen\n2-Üçgen")


if userAnswer=="1":
    kareKenar=[]
    for x in range (4):
        x=int(input("Dörtgen için kenar uzunluğu giriniz."))
        kareKenar.append(x)
    if kareKenar[0]==kareKenar[1] and kareKenar[1]==kareKenar[2] and kareKenar[2]==kareKenar[3]:
        print("Bu bir karedir.")
    else:
        print("Kare değildir. Sadece bir dörtgendir.")
        
elif userAnswer=="2":
    ucgenKenar=[]
    for x in range (3):
        x=int(input("Ucgen icin kenar uzunluğu giriniz."))
        ucgenKenar.append(x)
    if (abs(ucgenKenar[1]-ucgenKenar[2]) >= ucgenKenar[0]) or (ucgenKenar[0] >= (ucgenKenar[1]+ucgenKenar[2])):
        print("Bu kenarlar bir üçgen oluşturmuyor ki...")
    elif ucgenKenar[0]==ucgenKenar[1] and ucgenKenar[1]==ucgenKenar[2]:
        print("Bu bir eşkenar üçgendir.")
    elif (ucgenKenar[0]==ucgenKenar[1] and ucgenKenar[1]!=ucgenKenar[2]) or (ucgenKenar[0]==ucgenKenar[2] and ucgenKenar[0]!=ucgenKenar[1])or (ucgenKenar[1]==ucgenKenar[2] and ucgenKenar[0]!=ucgenKenar[1]):
        print("Bu bir ikizkenar üçgendir.")
    elif ucgenKenar[0]!=ucgenKenar[1] and ucgenKenar[1]!=ucgenKenar[2] and ucgenKenar[0]!=ucgenKenar[2]:
        print("Bu sıradan bir üçgendir.")
        
else:
    print("Geçerli bir seçim yapmadın...")
        