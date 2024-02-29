# Program Menentukan Tarif Pengiriman Paket

def tarif_berat(b):
    if b >= 1 and b <= 20:
        tarif_b = 10000
        print(f"Tarif dengan berat : {b}kg adalah Rp. ", tarif_b)
    elif b >= 21 and b <= 30:
        tarif_b = 15000
        print(f"Tarif dengan berat : {b}kg adalah Rp. ", tarif_b)
    elif b >= 31 and b <= 60:
        tarif_b = 20000
        print(f"Tarif dengan berat : {b}kg adalah Rp. ", tarif_b)
    elif b > 60:
        tarif_b = 45000
        print(f"Tarif dengan berat : {b}kg adalah Rp. ", tarif_b)
    else:
        tarif_b = 0
    
    return tarif_b


def tarif_jarak(j):
    if j >= 1 and j <= 5:
        tarif_j = 2000
        print(f"Tarif dengan jarak : {j}km adalah Rp. ", tarif_j)
    elif j >= 6 and j <= 15:
        tarif_j = 5000
        print(f"Tarif dengan jarak : {j}km adalah Rp. ", tarif_j)
    elif j >= 16 and j <= 30:
        tarif_j = 10000
        print(f"Tarif dengan jarak : {j}km adalah Rp. ", tarif_j)
    elif j > 30:
        tarif_j = 15000
        print(f"Tarif dengan jarak : {j}km adalah Rp. ", tarif_j)
    else:
        tarif_j = 0
    
    return tarif_j


def tarif_all(tb, tj):
    return tb + tj


print("Program Menentukan Tarif Pengiriman")
print("====================================")

while True: 
    berat = int(input("Inputkan berat\t: "))
    jarak = int(input("Inputkan jarak\t: "))
    print("------------------------------------")
    if berat <= 0 or jarak <= 0:
        if berat <= 0:
            print("Data berat yang anda inputkan tidak valid!")
        else:
            print("Data jarak yang anda inputkan tidak valid!")
        
        ulang = input("Ingin input ulang (Y/N) ? ")
        print("\n====================================")
        if ulang.lower() != 'y':
            print(f"\t-- Terima Kasih --".upper())
            break
        else:
            continue
    
    tBerat = int(tarif_berat(berat))
    tJarak = int(tarif_jarak(jarak))
    print("------------------------------------")
    tarif = int(tarif_all(tBerat, tJarak))
    print("Tarif keseluruhan : Rp. ", tarif)
    
    print(f"\n\t-- Terima Kasih --".upper())
    break

