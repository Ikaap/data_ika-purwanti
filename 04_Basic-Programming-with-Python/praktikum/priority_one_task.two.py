# Program Menghitung Volume Bola

phi = 3.14
def volume_bola(r):
    return 4/3 * phi * r ** 3

print("Program Menghitung Volume Bola")
print("====================================")
jari = float(input("Inputkan panjang jari-jari : "))

print("------------------------------------")
print("Panjang jari-jari : ", jari, "cm")
print("------------------------------------")

volume = volume_bola(jari)
print("Volume Bola : ", volume, "cm3")
print(f"\n\t-- Terima Kasih --".upper())
