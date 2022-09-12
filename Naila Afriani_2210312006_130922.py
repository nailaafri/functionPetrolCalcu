#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:39:10 2022

@author: yulizarw
"""



#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")
#mmeanggil fungsi untuk dapat  dijalankan
pengenalan_function()


#masukkan data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) 
def identitas_pembeli(nama,nomor_hape,pekerjaan):
   return (nama, nomor_hape, pekerjaan)

biodata_pembeli = identitas_pembeli("yudi", "0812345678", "kurir")


#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x),

#masukkan data bbm
tipe_bbm = jenis_bbm (("pertalait", "pertameks", "selar"))

#harga untuk pertalait = 10000, pertamek = 12000, selar = 5000
pertalait = 10000
pertameks = 12000
selar = 5000

#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan

def jenis_mobil (nama_brand,jumlah_liter):
    return (nama_brand, jumlah_liter)

#panggil fyungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil("honda", 3)

def hitung_biaya_bbm(liter, harga):
    total = liter * harga
   return total

#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm(identifikasi_kendaraan[1], pertameks)

print (total_belanja, "a")

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
nama = biodata_pembeli [0]
bbm = "selar"
print (f"yudi telah membeli bbm {bbm} seharga 12000 dengan total {total_belanja}")

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = uang - 360000
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang

print("\n\nRecursion Example Results")
belanja(720000)
#output jika uang 720000 dan total_belanja 360000
#0
#360000