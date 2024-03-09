# Program memasukkan sekumpulan karakter dari sebuah kata berdasarkan ruangan yang tersedia.

def collect_chars(word, rooms):
    word = word.replace(" ", "")
    chars = list(word)
    while len(chars) < rooms:
        chars.extend(chars)
    chars = chars[:rooms]
    
    return "".join(chars)

word1 = "alta"
rooms1 = 10
word2 = "sepulsa"
rooms2 = 20
word3 = "sepulsa mantap"
rooms3 = 20
print("Program Input Karakter berdasarkan ruangan yang tersedia")
print("==========================================================")
print("Test Case 1 :")
print(f"Word  : {word1}")
print(f"Rooms : {rooms1}")
print("-----------------------------")
print("Hasil : " + collect_chars(word1, rooms1))
print("\n")
print("Test Case 2 :")
print(f"Word  : {word2}")
print(f"Rooms : {rooms2}")
print("-----------------------------")
print("Hasil : " + collect_chars(word2, rooms2))
print("\n")
print("Test Case 3 :")
print(f"Word  : {word3}")
print(f"Rooms : {rooms3}")
print("-----------------------------")
print("Hasil : " + collect_chars(word3, rooms3))
print("==========================================================\n")
while True:
    pilih = input("Apakah ingin mencoba lagi (Y/N) ? ")
    if pilih.lower() == "y":
        word = input("Masukan word\t\t: ")
        rooms = int(input("Masukan banyak rooms\t: "))
        print("-----------------------------------------")
        print("Hasil : " + collect_chars(word, rooms) + "\n")
    else:
        print("\n==================================")
        print(f"\t-- Terima Kasih --".upper())
        break