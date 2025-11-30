#Expense Tracker Project

listExpenses = [] #List of all expenses

print("Welcome to Expense Tracker")

while True:
    print("====================== Menu ==========================")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter your choice : "))

    if(choice == 1 ):
        date = input("Enter Date : ")
        category = input("Enter Category Type like Travel, Food, Grocer : ")
        description = input("Enter short description (Optional) : ")
        amount = float(input("Enter amount : "))

        expenses = {
            "date": date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        listExpenses.append(expenses)
        print("epenses added in list!!")
    elif(choice == 2):
        if(len(listExpenses) > 0):
            count = 1
            print("========================== All expenses =====================")
            for item in listExpenses:
                print(f"| {count} | {item["date"]} | {item["category"]} | {item["amount"]} | {item["description"]}")
                count = count + 1

        else:
            print("please add expenses to press 1")
    elif(choice == 3):
        total = 0.0
        if(len(listExpenses) > 0):
            countTotal = 1
            print("========================== All expenses =====================")
            for item in listExpenses:
                total = total + float(item["amount"])
                countTotal = countTotal + 1
            print("Total Value : ", total)
        else:
            print("please add expenses to see your expenses")
    elif(choice == 4):
        print("Exit")
    else:
        print("Invalid option selected.....")
        break
