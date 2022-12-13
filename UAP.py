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

    def note():
  pilih = 0
  print("-------NOTE-------")
  nama_note = input("\nMasukkan nama file :")
  while pilih !=3:
    while(true):
      try:
        print("\n1 : Membuka",nama_note," \n2 : Menambah",nama_note," \n3 : Keluar Program")
        pilih = int(input("Pilih menu : "))
        if pilih<=0 or pilih>3 :
          raise ValueError
        print("")
        break
      except :
        print("pilih sesuai menu")
    
    if pilih == 1:
      try:
          innote = open(nama_note, "r")
          print("\nIsi dari",nama_note,":",innote.read())
          innote.close()
      except FileNotFoundError:
          print("note", nama_note , "Tidak ditemukan")
     
    elif pilih == 2:
      try:
          with open(nama_note, 'r') as nn:
            print("\nHasil dari",nama_note,": ")
            print(nn.read())
          isi = input("\nTambahkan teks ke file : ")
          outnote = open(nama_note, 'a')
          outnote.write("\n")
          outnote.write(isi)
          outnote = open(nama_note, 'r')
          print("Selamat : ",isi, "Berhasil ditambahkan pada File",nama_note,"\n") 
          print("\nIsi dari",nama_note,":",outnote.read())
          outnote.close()  
      except FileNotFoundError:
          print("Note",nama_note,"Tidak ditemukan ")
