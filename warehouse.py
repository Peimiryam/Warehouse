balance_account = 0

history = []

inventory = {}

print("Welcome to your warehouse software. These are the following commands: \n" )
print('''\n
    1. 'balance': add or subtract from the account.\n 
    2. 'sale': insert the name of the product, its price, and quantity and update the account \n 
    3. 'purchase': insert the name of the product, its price, and quantity and update the account\n 
    4. 'account': display the current account balance.\n 
    5. 'list': display the total inventory in the warehouse along with product prices and quantities.\n
    6. 'warehouse': display the product status in the warehouse.\n
    7. 'review': display recorded operations\n
    8. 'end': terminate the program\n''')

while True:

    print("\nCommands: 'balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end'.\n")
    command = input("Insert a command: ")

    if command == 'account':
        print(f"Total balance: {balance_account}" )

    elif command == 'end':
        print("\nHave a nice day :) Goodbye!")
        break

    elif command == 'balance':
        amount = float(input( "Insert a value: "))

        operation = input("Enter which operation would you like to perform? +/- ")

        if operation == '+':
            balance_account = balance_account + amount 
    
        elif operation == '-':

            if balance_account - amount < 0:
                print("Wrong input. ")
            elif balance_account - amount > 0:
                balance_account= balance_account - amount
        history.append(operation)
        history.append(amount)
    
    elif command == 'sale':
        item = input("Insert an item name: ")

        if item not in inventory:
            print("not available for sale")

        elif item in inventory:
            
            quantity = int(input("Insert a quantity: "))
#not working
            if inventory[item] < quantity:
                print("Not enough quantity")

            else:
                inventory[item] -= quantity

            price = float(input("Insert a price: "))
            balance_account = balance_account + price * quantity
            history.append(f"Name: {item}")
            history.append(f"Price: {price}")
            history.append(quantity)
            
    elif command == 'purchase':
        item = input("Insert an item name: ")
        quantity = int(input("Insert a quantity: "))
        price = float(input("Insert a price: "))

        if balance_account - price > 0:
            balance_account = balance_account - price * quantity
            history.append(f"Price: {price}")
            history.append(f"Name: {item}")
            history.append(quantity)
            inventory[item] = quantity, price
            print(item + "\nQuantity: " + str(quantity) + "\nPrice: " + str(price))

        elif balance_account - price < 0:
            print("Not enough amount. ")
   
    elif command == 'list':

        if len(inventory) == 0:
            print("No record found")
        else:
            print(inventory)

    elif command == 'warehouse':
        search = input("Insert the name of the item you want to search: ")

        if search in inventory:
            print("Item found. ")

            ware = inventory.get(search)

            print(ware)

        else:
            print("Not available")

    elif command == 'review':

        log = input("Press 'all' to see all history or 'range' to input range values")

        if log == 'all':
            print(history)

        elif log == 'range':

            print("Insert a from and to value to see the history: ")
        from_value = int(input("From: "))
        to_value = int(input("To: "))

        lenght = len(history)
        
        print(history[from_value : to_value])
