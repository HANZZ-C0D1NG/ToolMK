"""Tools Matematika By HANZZ"""

import os

# Menu utama
def menu_utama():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.0\n")
  menu = input("Menu utama:\n[0] Keluar\n[1] Kalkulator\n[2] Kredit\n\nPilih menu: ")
  if menu == "0":
     print("Berhasil keluar")
     exit()
  elif menu == "1":
       menu_satu()
  elif menu == "2":
       kredit()
  else:
      print("Perintah tidak valid!")
      exit()

# Menu satu
def menu_satu():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.0\n")
  menu = input("Menu satu:\n[0] Kembali\n[1] Penjumlahan\n[2] Pengurangan\n[3] Perkalian\n[4] Pembagian\n\nPilih menu: ")
  if menu == "0":
     menu_utama()
  elif menu == "1":
       penjumlahan()
  elif menu == "2":
       pengurangan()
  elif menu == "3":
       perkalian()
  elif menu == "4":
       pembagian()
  else:
      print("Perintah tidak valid!")

# Credit
def kredit():
  os.system("clear")
  print("Bantu support nya cuy, dengan cara memberikan star.\n\nGithub:HANZZ-C0D1NG\nRepository:ToolMK")

# Tools kalkulator
def penjumlahan():
  os.system("clear")
  print("=====Penjumlahan=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a + b
  print("Hasil dari", a, "+", b, "=", c)

def pengurangan():
  os.system("clear")
  print("=====Pengurangan=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a - b
  print("Hasil dari", a, "-", b, "=", c)

def perkalian():
  os.system("clear")
  print("=====Perkalian=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a * b
  print("Hasil dari", a, "x", b, "=", c)

def pembagian():
  os.system("clear")
  print("=====Pembagian=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a / b
  print("Hasil dari", a, ":", b, "=", c)

menu_utama()