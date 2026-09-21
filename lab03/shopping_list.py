#Setting variables
grocery_list = []


#Interface
print('''Welcome to Your Shopping List!
 
Please make a selection from one of the following options:
 
1. Add an item to the shopping list.
2. Display the shopping list.
3. Display the item count.
4. Display the first item in the shopping list.
5. Display the last item in the shopping list.
6. Clear the shopping list.
''')
selection = input('Selection: ')

while 1:
    if selection == '1':
        grocery_list.append(input('Item to add: '))
        break
    elif selection == '2':
        print(grocery_list)
        break
    elif selection == '3':
        print(f'ITEM COUNT: {grocery_list.count}')
        break
    elif selection == '4':
        print(grocery_list[0])
        break
    elif selection == '5':
        print(grocery_list[-1])
        break
    elif selection == '6':
        grocery_list = []
        break
    else:
        print('Please enter a valid option')