# Program Memeriksa suatu kata Anagram

def anagram(kSatu, kDua):
    kSatu = kata_satu.replace(" ", "")
    kDua = kata_dua.replace(" ", "")
    if sorted(kSatu) == sorted(kDua):
        print(f"{kSatu} dan {kDua} merupakan \033[1mAnagram\033[0m")
    else:
        print(f"{kSatu} dan{kDua} merupakan \033[1mBukan Anagram\033[0m")


print("Program Memeriksa suatu kata Anagram")
print("====================================")

kata_satu = input("Masukkan kata pertama\t: ")
kata_dua = input("Masukkan kata kedua\t: ")
print("------------------------------------")
anagram(kata_satu, kata_dua)
