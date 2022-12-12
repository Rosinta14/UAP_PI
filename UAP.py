import json, requests
import os
from HariLibur import *
data0=requests.get('https://api-harilibur.vercel.app/api')
data1=data0.json()
while True:
  found=False
  menu()
  pilih=int(input("Masukkan Pilihanmu (1-3) : "))
  if pilih==1:
    for data in data1:
      hari=HariLibur(data)
      hari.show()
  elif pilih==2: 
    cari=input("Masukkan Tanggal (YYYY-MM-D / MM-D) : ")
    print()
    for data in data1:
      if data['holiday_date'].find(cari)!=-1:
        hari=HariLibur(data)
        hari.show()
    if found==False:
      print("Hari tidak ditemukan\n")
  elif pilih==3:
    cari=input("Masukkan Nama Hari Nasional : ")
    print()
    for data in data1:
      if data['holiday_name'].lower().find(cari.lower())!=-1:
        hari=HariLibur(data)
        hari.show()
    if found==False:
      print("Hari tidak ditemukan\n")
  elif pilih==4:
    break
  else:
    print("\nPilihan anda salah!\nSilahkan coba lagi\n")
