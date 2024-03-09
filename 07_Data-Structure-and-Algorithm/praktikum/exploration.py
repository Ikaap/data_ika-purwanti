# Program Mengelola Data Pengeluaran

import uuid

class Expense():
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount
        self.list_expenses_data = []
        
    def information(self):
        return "Id\t: " + str(self.id) + "\n" + "Name\t: " + self.name + " \n" + "Amount\t: Rp. " + str(self.amount)

    def create_expense(self, name, amount):
        new_expense_data = Expense(str(uuid.uuid4()), name, amount)
        self.list_expenses_data.append(new_expense_data)
        print("Data added!\n")
    
    def view_expense(self):
        total = 0
        if not self.list_expenses_data:
            print("There is no expenditure data yet\n")
        else:
            print("All Expenses")
            print("-----------------")
            for expense_data in self.list_expenses_data:
                print(expense_data.information())
                print("-------------------------------")
                total += int(expense_data.amount)
            print(f"TOTAL : Rp. {total}")
    
    def update_expense(self, id, name_update, amount_update):
        for expense_data in self.list_expenses_data:
            if expense_data.id != id:
                print(f"Expenditure data with {id} not found!\n")
            else:
                expense_data.name = name_update
                expense_data.amount = amount_update
                print("Data updated!\n")
                return
    
    def delete_expense(self, id):
        for expense_data in self.list_expenses_data:
            if expense_data.id != id:
                print(f"Expenditure data with {id} not found!\n")
            else:
                self.list_expenses_data.remove(expense_data)
                print("Data deleted!\n")
                return



print("Program Mengelola Data Pengeluaran")
print("===================================")

# deklarasi object
expense_data = Expense("", "", 0)

while True:
    print("==============  MENU  =============")
    print("1. Create new expense data")
    print("2. View expense")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Exit")
    print("-------------------------------")
    menu = input("Enter your choice : ")
    if menu == "1":
        name = input("Enter expense name : ")
        amount = int(input("Enter amount : "))
        if name != None and amount != None :
            expense_data.create_expense(name, amount)
            
    elif menu == "2":
        expense_data.view_expense()
        
    elif menu == "3":
        id = input("Enter expenses id : ")
        name_update = input("Enter expense name : ")
        amount_update = input("Enter amount : ")
        if id != None and name != None and amount != None :
            expense_data.update_expense(str(id), name_update, str(amount_update))
            
    elif menu == "4":
        id = input("Enter expenses id : ")
        if id != None:
            expense_data.delete_expense(str(id))
            
    elif menu == "5":
        print("Bye...")
        print("\n====================================")
        print(f"\t-- Terima Kasih --".upper())
        break
    else:
        print("The menu you selected is not available")