# Program Menentukan Jenis Roti berdasarkan Jumlah Tepung

def get_breads(breads, flour_stock):
    name_of_bread = []
    sorted_breads_by_flour = sorted(breads, key=lambda x: x["flour"])
    
    for bread in sorted_breads_by_flour:
        if bread["flour"] <= flour_stock:
            flour_stock -= bread["flour"]
            name_of_bread.append(bread["name"])
    
    return name_of_bread


bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
    {"name": "pancake", "flour": 15},
    {"name": "waffle", "flour": 25},
    {"name": "bagel", "flour": 15},
    {"name": "cupcake", "flour": 15},
    {"name": "choco chips", "flour": 10},
    {"name": "mini puff", "flour": 5},
    {"name": "bread", "flour": 30},
]
flour_stock1 = 100
flour_stock2 = 75

print("Program Menentukan Jenis Roti berdasarkan Jumlah Tepung")
print("======================================================")
print("Daftar Roti 1 :")
for i in range(len(bread1)):
    print(f"{i+1}. Name : {bread1[i]["name"]}, Flour : {bread1[i]["flour"]}kg ")
print("------------------------------")
print(f"Target : {flour_stock1}kg")
print("==============================")
print("Jenis roti yang dapat dibuat : ")
breads = get_breads(bread1, flour_stock1)
for i in range(len(breads)):
    print(f"{i+1}. " + breads[i])
print("======================================================\n")
print("Daftar Roti 2 :")
for i in range(len(bread2)):
    print(f"{i+1}. Name : {bread2[i]["name"]}, Flour : {bread2[i]["flour"]}kg ")
print("------------------------------")
print(f"Target : {flour_stock2}kg")
print("==============================")
print("Jenis roti yang dapat dibuat : ")
breads = get_breads(bread2, flour_stock2)
for i in range(len(breads)):
    print(f"{i+1}. " + breads[i])