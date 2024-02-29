# Program Mencetak angka 1 - 100 dengan kriteria tertentu

print("Program Mencetak angka 1 - 100")
print("====================================")
for i in range(1, 101):
    if i  % 3 == 0 and i  % 5 == 0:
        print("buzz")
    elif i  % 3 == 0:
        print(f"{i**2}")
    elif i % 5 == 0:
        print(f"{i**3}")
    else:
        print(i,)