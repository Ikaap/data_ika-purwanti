# Program Mengelompokkan Sekumpulan Bilangan berdasarkan Target Kelipatan

def group_numbers(numbers, target):
    bil_kelipatan = []
    not_bil_kelipatan = []
    for x in range(len(numbers)):
        if numbers[x] % target == 0:
            bil_kelipatan.append(numbers[x])
        else:
            not_bil_kelipatan.append(numbers[x])
    return [f"{bil_kelipatan}, {not_bil_kelipatan}"]

number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 3

number2 = [23, 15, 19, 20, 75, 30, 45]
target2 = 5

print("Program Mengelompokkan Sekumpulan Bilangan berdasarkan Target Kelipatan")
print("=========================================================================")
print("Bilangan 1:")
for i in range(len(number1)):
    print(number1[i], end=', ')
print("\n------------------------------")
print(f"Target : {target1}")
print("==============================")
print(f"Hasil : {group_numbers(number1, target1)}")
print("\n-------------------------------------------------------")
print("Bilangan 2:")
for i in range(len(number2)):
    print(number2[i], end=', ')
print("\n------------------------------")
print(f"Target : {target2}")
print("==============================")
print(f"Hasil : {group_numbers(number2, target2)}")