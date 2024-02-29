# Program Menentukan Priotitas Sebuah Proyek

def skor_budget(b):
    if b >= 0 and b <= 50:
        skor_b = 4
        print(f"Skor dengan budget\t\t: {b} adalah ", skor_b)
    elif b >= 51 and b <= 80:
        skor_b = 3
        print(f"Skor dengan budget\t\t: {b} adalah ", skor_b)
    elif b >= 81 and b <= 100:
        skor_b = 2
        print(f"Skor dengan budget\t\t: {b} adalah ", skor_b)
    elif b > 100:
        skor_b = 1
        print(f"Skor dengan budget\t\t: {b} adalah ", skor_b)
    else:
        skor_b = 0
    
    return skor_b


def skor_waktu(w):
    if w >= 0 and w <= 20:
        skor_w = 10
        print(f"Skor dengan waktu pengerjaan\t: {w} adalah ", skor_w)
    elif w >= 21 and w <= 30:
        skor_w = 5
        print(f"Skor dengan waktu pengerjaan\t: {w} adalah ", skor_w)
    elif w >= 31 and w <= 50:
        skor_w = 2
        print(f"Skor dengan waktu pengerjaan\t: {w} adalah ", skor_w)
    elif w > 50:
        skor_w = 1
        print(f"Skor dengan waktu pengerjaan\t: {w} adalah ", skor_w)
    else:
        skor_w = 0
    
    return skor_w


def skor_kesulitan(k):
    if k >= 0 and k <= 3:
        skor_k = 10
        print(f"Skor dengan tingkat kesulitan\t: {k} adalah ", skor_k)
    elif k >= 4 and k <= 6:
        skor_k = 5
        print(f"Skor dengan tingkat kesulitan\t: {k} adalah ", skor_k)
    elif k >= 8 and k <= 10:
        skor_k = 1
        print(f"Skor dengan tingkat kesulitan\t: {k} adalah ", skor_k)
    elif k > 10:
        skor_k = 0
        print(f"Skor dengan tingkat kesulitan\t: {k} adalah ", skor_k)
    else:
        skor_k = 0
    
    return skor_k


def skor_all(sb, sw, sk):
    return sb + sw + sk

def cek_prioritas(sAll):
    if sAll <= 24 and sAll >= 17:
        print("High")
    elif sAll <= 16 and sAll >= 10:
        print("Medium")
    elif sAll <= 9 and sAll >= 3:
        print("Low")
    elif sAll <= 2:
        print("Impossible")
    else:
        print("Invalid")


print("Program Menentukan Priotitas Proyek")
print("====================================")

while True: 
    budget = int(input("Inputkan budget\t\t\t: "))
    waktu = int(input("Inputkan waktu pengerjaan\t: "))
    kesulitan = int(input("Inputkan tingkat kesulitan\t: "))
    print("------------------------------------")
    if budget < 0 or waktu < 0 or kesulitan < 0:
        if budget < 0:
            print("Data budget yang anda inputkan tidak valid!")
        elif waktu < 0:
            print("Data waktu pengerjaan yang anda inputkan tidak valid!")
        else:
            print("Data tingkat kesulitan yang anda inputkan tidak valid!")
        
        ulang = input("Ingin input ulang (Y/N) ? ")
        print("\n====================================")
        if ulang.lower() != 'y':
            print(f"\t-- Terima Kasih --".upper())
            break
        else:
            continue
    
    sBudget = int(skor_budget(budget))
    sWaktu = int(skor_waktu(waktu))
    sKesulitan = int(skor_kesulitan(kesulitan))
    print("------------------------------------")
    skor = int(skor_all(sBudget, sWaktu, sKesulitan))
    print("Skor keseluruhan : ", skor)
    cek_prioritas(skor)
    
    
    print(f"\n\t-- Terima Kasih --".upper())
    break