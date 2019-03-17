#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:22:56 2019

@author: ipekgamzeucal
"""
import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı", kanal="tv8", ses=0, kanallar=["tv8"]):
        self.tv_durum=tv_durum
        self.kanal=kanal
        self.ses=ses
        self.kanallar=kanallar
        
    def tv_aç(self):
        if self.tv_durum=="Açık":
            print("TV Zaten Açık...")
        else:
            print("TV Açılıyor...")
            self.tv_durum="Açık"
    def tv_kapat(self):
        if self.tv_durum=="Kapalı":
            print("TV'yi kapatmadan önce açman gerekir...")
        else:
            print("Si yaa.. -_- ")
            self.tv_durum="Kapalı"
    def volume(self):
        while True:
            volumeAyar=input("Sesi azaltmak için: '<', sesi artırmak için: '>', çıkmak için:'q'...")
            
            if volumeAyar==">" and self.ses!=32:
                self.ses+=1
                print("Ses:",self.ses)
            elif volumeAyar=="<" and self.ses!=0:
                self.ses-=1
                print("Ses:",self.ses)
            elif volumeAyar=="q":
                print("Güncel ses:",self.ses)
                break
    def kanalEkleme(self,kanalAdı):
        self.kanallar.append(kanalAdı)
        print("Güncel kanal listesi:",self.kanallar)
    def kanalSilme(self,kanalAdı):
        self.kanallar.remove(kanalAdı)
        print("Güncel kanal listesi:",self.kanallar)
    def kanalListeleme(self,kanallar):
        print(self.kanallar," Toplam Kanal Sayısı: ",len(kanallar))
    def kanalDeğiştir(self):
        randomIndex=random.randint(0,len(self.kanallar)-1)
        self.kanal=self.kanallar[randomIndex]
        print("Güncel kanal:",self.kanal)
    def __len__(self):
        return len(self.kanallar)

kumandam=Kumanda()

print("""
*******************  
TV-Kumanda Uygulaması

1-TV Aç
2-TV Kapat
3-Kanal Listele
4-Kanal Ekleme
5-Kanal Silme
6-Kanal Sayısı
7-Rastgele Kanal
8-Ses Ayarla
9-Çıkış

*******************  
""")

while True:
    uw=input("Yapmak istediğiniz işlemi girin:")
    
    if uw=="9":
        print("Bye Bye Happiness!")
        break
    elif uw=="1":
        kumandam.tv_aç()
    elif uw=="2":
        kumandam.tv_kapat()
    elif uw=="3":
        kumandam.kanalListeleme(kumandam.kanallar)
    elif uw=="4":
        kanal=input("Hangi Kanal Eklensin?")
        kumandam.kanalEkleme(kanal)
    elif uw=="5":
        kanal=input("Hangi Kanal Silinsin?")
        kumandam.kanalSilme(kanal)
    elif uw=="6":
        print("Kanal Sayısı:",kumandam.__len__())
    elif uw=="7":
        kumandam.kanalDeğiştir()
    elif uw=="8":
        kumandam.volume()
    else:
        break

print("TV Kumanda Uygulamasından Çıkış Yaptınız...")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            