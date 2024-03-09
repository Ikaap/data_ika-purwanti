# Program Prima Segiempat

def prime_rectangle(height, width, start):
    def is_prime(angka):
        if angka <= 1:
            return False
        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                return False
        return True

    sum = 0
    start = start + 1
    for i in range(width):
        for x in range(height):
            while not is_prime(start):
                start += 1
            print(start, end=' ')
            sum += start
            start += 1
        print()
    print(sum)
    
    return sum

height1 = 2
width1 = 3
start1 = 13

height2 = 5
width2 = 2
start2 = 1

print("Program Prima Segiempat")
print("=======================")
print("Prima Segiempat 1")
print(f"Height\t: {height1}")
print(f"Width\t: {width1}")
print(f"Start\t: {start1}")
print("=======================")
print("Hasil : ")
prime_rectangle(height1, width1, start1)
print("\n=======================")
print("Prima Segiempat 2")
print(f"Height\t: {height2}")
print(f"Width\t: {width2}")
print(f"Start\t: {start2}")
print("=======================")
print("Hasil : ")
prime_rectangle(height2, width2, start2)
print("==========================================================\n")
while True:
    pilih = input("Apakah ingin mencoba lagi (Y/N) ? ")
    if pilih.lower() == "y":
        height = int(input("Masukan height\t: "))
        width = int(input("Masukan width\t: "))
        start = int(input("Masukan start\t: "))
        print("-----------------------------------------")
        print("Hasil : ")
        prime_rectangle(height, width, start)
    else:
        print("\n==================================")
        print(f"\t-- Terima Kasih --".upper())
        break