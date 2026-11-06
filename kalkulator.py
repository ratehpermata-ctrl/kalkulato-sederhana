#kalkulator

def tambah(a, b):
    print("Hasilnya:", a + b)

def kurang(a, b):
    print("Hasilnya:", a - b)

def kali(a, b):
    print("Hasilnya:", a * b)

def bagi(a, b):
    if b == 0:
        print("Gak bisa dibagi 0!")
    else:
        print("Hasilnya:", a / b)

print("****** KALKULATOR ******")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilih = input("Pilih 1-4: ")
angka1 = float(input("Masukin angka pertama: "))
angka2 = float(input("Masukin angka kedua: "))

if pilih == "1":
    tambah(angka1, angka2)
elif pilih == "2":
    kurang(angka1, angka2)
elif pilih == "3":
    kali(angka1, angka2)
elif pilih == "4":
    bagi(angka1, angka2)
else:
    print("Pilihanmu salah, pilih 1-4 aja!")