"""Tools Matematika By HANZZ"""

import os

# Menu utama
def menu_utama():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  menu = input("Menu utama:\n[0] Keluar\n[1] Kalkulator\n[2] Pangkat dan akar\n[3] Kredit\n\nPilih menu: ")
  if menu == "0":
     print("Berhasil keluar")
     exit()
  elif menu == "1":
       kalkulator_menu()
  elif menu == "2":
       pangkat_akar()
  elif menu == "3":
       kredit()
  else:
      print("\nPerintah tidak valid!\n")
      exit()

# Kalkulator menu
def kalkulator_menu():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  menu = input("Kalkulator menu:\n[0] Kembali\n[1] Penjumlahan\n[2] Pengurangan\n[3] Perkalian\n[4] Pembagian\n[5] Penjumlahan desimal\n[6] Pengurangan desimal\n[7] Perkalian desimal\n[8] Pembagian desimal\n\nPilih menu: ")
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
  elif menu == "5":
       penjumlahan_desimal()
  elif menu == "6":
       pengurangan_desimal()
  elif menu == "7":
       perkalian_desimal()
  elif menu == "8":
       pembagian_desimal()
  else:
      print("Perintah tidak valid!")

# Pangkat dan akar menu
def pangkat_akar():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  menu = input("Pangkat & akar menu:\n[0] Kembali\n[1] Pangkat dua\n[2] Pangkat tiga\n[3] Akar pangkat dua\n[4] Akar pangkat tiga\n\nPilih menu: ")
  if menu == "0":
     menu_utama()
  elif menu == "1":
       pangkat_dua()
  elif menu == "2":
       pangkat_tiga()
  elif menu == "3":
       akar_pangkat_dua()
  elif menu == "4":
       akar_pangkat_tiga()
  else:
      print("Perintah tidak valid!")

# Credit
def kredit():
  os.system("clear")
  print("Bantu support nya cuy, dengan cara memberikan star.\n\nGithub:HANZZ-C0D1NG\nRepository:ToolMK")

# Kalkulator
def penjumlahan():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====Penjumlahan=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a + b
  print("Hasil dari", a, "+", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def pengurangan():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====Pengurangan=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a - b
  print("Hasil dari", a, "-", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def perkalian():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====Perkalian=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a * b
  print("Hasil dari", a, "x", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def pembagian():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====Pembagian=====")
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))
  c = a // b
  print("Hasil dari", a, ":", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def penjumlahan_desimal():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PenjumlahanDesimal=====")
  a = float(input("Masukkan angka pertama: "))
  b = float(input("Masukkan angka kedua: "))
  c = a + b
  print("Hasil dari", a, "+", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def pengurangan_desimal():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PenguranganDesimal=====")
  a = float(input("Masukkan angka pertama: "))
  b = float(input("Masukkan angka kedua: "))
  c = a - b
  print("Hasil dari", a, "-", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def perkalian_desimal():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PerkalianDesimal=====")
  a = float(input("Masukkan angka pertama: "))
  b = float(input("Masukkan angka kedua: "))
  c = a * b
  print("Hasil dari", a, "x", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def pembagian_desimal():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PembagianDesimal=====")
  a = float(input("Masukkan angka pertama: "))
  b = float(input("Masukkan angka kedua: "))
  c = a / b
  print("Hasil dari", a, ":", b, "=", c)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()
  
# Pangkat dan akar
def pangkat_dua():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PangkatDua=====")
  nilai = int(input("Masukkan nilai yang ingin di pangkatkan: "))
  hasil = nilai ** 2
  print("Hasil dari", nilai, "pangkat dua =", hasil)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def pangkat_tiga():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====PangkatTiga=====")
  nilai = int(input("Masukkan nilai yang ingin di pangkatkan: "))
  hasil = nilai ** 3
  print("Hasil dari", nilai, "pangkat tiga =", hasil)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()

def akar_pangkat_dua():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====AkarPangkatDua=====")
  nilai = int(input("Masukkan nilai yang ingin diakar: "))
  hasil = nilai ** 0.5
  if hasil.is_integer():
     hasil = int(hasil)
     print("Akar pangkat dua dari", nilai, "=", hasil)
  else:
      print("Akar pangkat dua dari", nilai, "=", hasil)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()
       
def akar_pangkat_tiga():
  os.system("clear")
  print("=====ToolMK=====")
  print("Pembuat: HANZZ-C0D1NG")
  print("Versi: 1.0.8\n")
  print("=====AkarPangkatTiga=====")
  nilai = int(input("Masukkan nilai yang ingin diakar: "))
  hasil = nilai ** (1/3)
  hasil = round(hasil, 10)
  if hasil.is_integer():
     hasil = int(hasil)
     print("Akar pangkat tiga dari", nilai, "=", hasil)
  else:
      print("Akar pangkat tiga dari", nilai, "=", hasil)
  confirm = input("\nKembali ke menu utama? (y/n): ")
  if confirm == "y":
     menu_utama()
  else:
      print("\n")
      exit()
      
menu_utama()