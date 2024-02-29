# Program Menghitung Luas Persegi Panjang dan Menentukan Even atau Odd Rectangle

def luas_persegi_panjang(p, l):
    return p * l

def cek_hasil_luas(luas_persegi_panjang):
    if luas_persegi_panjang % 2 == 0:
        print(f"Luas Persegi Panjang = {luas_persegi_panjang} cm2, Even Rectangle")
    else:
        print(f"Luas Persegi Panjang = {luas_persegi_panjang} cm2, Odd Rectangle")


print("Program Menghitung Luas Persegi")
print("====================================")
panjang = int(input("Inputkan panjang sisi\t: "))
lebar = int(input("Inputkan lebar sisi\t: "))

print("------------------------------------")
print("Panjang sisi\t: ", panjang, "cm")
print("Lebar sisi\t: ", lebar, "cm")
print("------------------------------------")

luas = luas_persegi_panjang(panjang, lebar)
cek_hasil_luas(luas)
print(f"\n\t-- Terima Kasih --".upper())
