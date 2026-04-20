"""The data files are created and opened once at the start of the program before going through the rest of it. 
   The baskets are calculated by saying if the values of all items are greater than zero and equal to each other it adds a basket
   The top5 and bottom5 use the sorted function, which at first calls inventory into a tuple so it can use the two seperate values inside of it
   then it uses lambda as a mini function to sort the list by item quantities instead of alphabetically, then for top five the reverse=True, reverses it from it's origional value
   of smallest to largest to largest to smallest quantities, then for the [:5] it just means it only takes the first five items"""
import os
import datetime
current_date = datetime.datetime.now()#get today's date


# Creates both files as soon as program is run
def invExist(): 
    #if file doesn't exist: create it and write the list on it
    if not os.path.exists("inventory.txt"):

        file = open('inventory.txt','w')
        file.write("ham:0 \nyams:0 \ngreen beans:0 \npeas:0 \npumpkin:0 \nmashed potatoes: 0 \nsugar:0 \ncranberry sauce:0 \npie filling:0 \ngravy mix:0 \ncookie mix:0 \ncooking oil:0 \nturkey:0 \ncorn:0 \ncarrots:0 \nfruit:0 \nmilk:0 \npotatoes:0 \nflour:0 \npie crust:0 \nstuffing mix:0 \nbread mix:0 \ncake mix and icing:0 \nmac n cheese:0 \ncanned meats:0 \npeanut butter:0 \ncanned soup:0 \nquick meals:0 \nboxed meal kits:0")
        file.close()
    #Create a dictionary and take every value inside of the txt file and shove it into it
    inventory = {}
    with open('inventory.txt', 'r') as f:
        for line in f:
            item, qty = line.strip().split(":")
            inventory[item] = int(qty)

    #if file doesn't exist: create it and write format the logs will follow
    if not os.path.exists('transaction.txt'):

        transaction = open('transaction.txt', 'w')
        transaction.write("Month-DD-YYYY HH:MM (AM/PM) | UPDATE | Item Name - Quantity")
        transaction.write('\n')
        transaction.close()
    return inventory



#Point dictionary
p_dict = {
    'ham': 50,
    'yams': 5,
    'green beans': 5,
    'peas': 5,
    'pumpkin': 5,
    'mashed potatoes': 8,
    'sugar': 15,
    'cranberry sauce': 5,
    'pie filling': 5,
    'gravy mix': 1,
    'cookie mix': 5,
    'cooking oil': 8,
    'turkey': 50,
    'corn': 5,
    'carrots': 5,
    'fruit': 5,
    'milk': 5,
    'potatoes': 5,
    'flour': 10,
    'pie crust': 8,
    'stuffing mix': 10,
    'bread mix': 5,
    'cake mix and icing': 5,
    'mac n cheese': 2,
    'canned meats': 10,
    'peanut butter': 8,
    'canned soup': 5,
    'quick meals': 1,
    'boxed meal kits': 5
}


#View category selection
def view(inventory):
    try:
        op = input("Would you like: Whole List, Search Item, Baskets, Top 5, or Bottom 5? ").lower()
        if op == 'whole list':
            wholeList()
  

        elif op == 'search item':
            searchItem()


        elif op.lower() == 'baskets':
            baskets()

        elif op == 'top 5':
            top5()

        
        elif op == 'bottom 5':
            bottom5()
        else:
            print("You might've mispelled that")
    except Exception:
        print("Something went wrong with on one the view() functions")



#Updating values to the txt file
def update(inventory):
    item = input('What item quantity do you want to change? ')
    qty = int(input('How many items do you have now? '))
    #if value < 0 raise an exception error
    if int(qty) < 0:
        raise Exception("You can't have a negative number")
    else:
        #If input in dictionary, take both value and item and reset it to blank
        if item in inventory:
            inventory[item] = int(qty)
            with open('inventory.txt', 'w') as file:
                file.write('')
            #For every item in inventory, open the file and rewrite everything inside of dictionary, including the changed value
            for i in inventory:
                with open('inventory.txt', 'a') as file:
                    file.write(i)
                    file.write(': ')
                    file.write(str(inventory[i]))
                    file.write('\n')
            #Open the transaction file and write the current date month-day-year | hour:minute am/pm | and then item name and how many items there are after change
            with open('transaction.txt', 'a') as trans:
                trans.write(current_date.strftime("%b-%d-%Y | %I:%M %p"))
                trans.write(' | ')
                trans.write('UPDATE')
                trans.write(' | ')
                trans.write(item)
                trans.write(' - ')
                trans.write(str(qty))
                trans.write('\n')
        #If item not in dictionary ask if they want to add item, and if so rewrite everything in inventory.txt
        else: 
            add = input('Do you wish to add that item? ')
            if add.lower() == 'yes' or 'y':
                inventory[item] = int(qty)
            with open('inventory.txt', 'w') as file:
                file.write('')
            #For every item in inventory, open the file and rewrite everything inside of dictionary, including the changed value
            for i in inventory:
                with open('inventory.txt', 'a') as file:
                    file.write(i)
                    file.write(': ')
                    file.write(str(inventory[i]))
                    file.write('\n')
            #Open the transaction file and write the current date month-day-year | hour:minute am/pm | and then item name and how many items there are after change
            with open('transaction.txt', 'a') as trans:
                trans.write(current_date.strftime("%b-%d-%Y | %I:%M %p"))
                trans.write(' | ')
                trans.write('UPDATE')
                trans.write(' | ')
                trans.write(item)
                trans.write(' - ')
                trans.write(str(qty))
                trans.write('\n')



#View the whole list          
def wholeList():
    print('\nInventory List:')
    total_qty = sum(inventory.values())
    total_points = 0
    #For every iteration in inventory multiply points by quantity of that item and add them together
    for item, qty in inventory.items():
        # use p_dict (if present) for per-item point weight, default to 1
        weight = p_dict.get(item, 1)
        points = int(qty) * int(weight)
        total_points += points
        #Print item name, it's quantity, how many points it's worth, and how many points you have
        print(f"Item: {item} | Quantity: {qty} | Point value: {weight} | Cumulative points: {points}")
    #Print the total amount of points and quantity of each item you have
    print(f'\nThe total amount of items is {total_qty}')
    print(f'The total amount of points is {total_points}')



#input item you want to see and print item name, it's quantity, how many points it's worth, and how many points you have
def searchItem():
        choice = input('Enter the item name: ').strip().lower()#.strip() gets rid of whitespace
        if choice in inventory:
            print(f"Item: {choice} | Quantity: {inventory[choice]} | Cumulative Points: {p_dict[choice]*inventory[choice]}")
        else:
            #if it's not there say it isn't on the list
            print(f"{choice} isn't in the list.")



def baskets():
    #Make a list, and if there aren't enough item quantities for each item, say what is missing
    basket = ['ham' , 'yams' , 'green beans' , 'peas', 'pumpkin', 'mashed potatoes', 'sugar', 'cranberry sauce', 'pie filling', 'gravy mix', 'cookie mix', 'cooking oil', 'turkey', 'corn', 'carrots', 'fruit', 'milk', 'potatoes', 'flour', 'pie crust', 'stuffing mix', 'bread mix', 'cake mix and icing', 'mac n cheese']
    missing = [i for i in basket if i not in inventory]
    if missing:
        print('The following items are missing from the inventory:', ', '.join(missing))
    else:
        #Print how many baskets you have by checking if each item quantity is greater than zero, and it prints the smallest value
        complete_basket = min(inventory[item] for item in basket)
        if complete_basket > 0:
            print(f'Complete baskets: {complete_basket}')
        else:
            #Print there are zero total baskets
            print('Total baskets: 0')



def top5():
    #Sorts the list from largest to smallest value and only takes top 5 values
    top5 = sorted(inventory.items(), key=lambda x: x[1], reverse=True)[:5]
    for item, qty in top5:
        print(f"{item}: {qty}")



def bottom5():
    #Sorts the list from smallest to largest value and only takes bottom 5 values
    bottom5 = sorted(inventory.items(), key=lambda x: x[1])[:5]
    for item, qty in bottom5:
        print(f"{item}: {qty}")


#Make inventory = inveExist function's return
inventory = invExist()
decide = str(input("Would you like to View or Update?: ").lower())

if decide == 'view':
    view(inventory)
elif decide == 'update':
    update(inventory)
else:
    print("You might've mispelled your choice.")