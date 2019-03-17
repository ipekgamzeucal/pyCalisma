#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:24:29 2019

@author: ipekgamzeucal
"""

class Bilgisayar():
    
    def __init__(self,Marka="Bilgi Yok",Model="Bilgi Yok",Renk="Bilgi Yok",EkranBoyutu="Bilgi Yok",İşlemci="Bilgi Yok",RAM="Bilgi Yok"):
        print("Bilgisayar oluşturuluyor :)")
        self.Marka=Marka
        self.Model=Model
        self.Renk=Renk
        self.EkranBoyutu=EkranBoyutu
        self.İşlemci=İşlemci
        self.RAM=RAM
    
    def __str__(self):
        return "Marka:{}, Model:{}, Renk:{}, EkranBoyutu:{}, İşlemci:{}, RAM:{}".format(self.Marka,self.Model,self.Renk,self.EkranBoyutu,self.İşlemci,self.RAM)
    
    def __len__(self):
        return "EkranBoyutu:{}".format(self.EkranBoyutu)
    
    def __del__(self):
        print("Bilgisayar yokediliyor :)")
    
bilg=Bilgisayar("Apple","MacBook Pro","Uzay Grisi","13'","i5","16GB")


print(bilg)

del(bilg)