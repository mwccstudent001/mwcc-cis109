#Setting variables
grocery_list = ['apple', 'bannana', 'cranberries']

while 1:

    #Interface
    print('''Welcome to Your Shopping List!
    
    Please make a selection from one of the following options:
    
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Exit
    ''')
    selection = input('Selection: ')

    if selection == '1':
        added_item = (input('Item to add: '))
        grocery_list.append(added_item)
        input('Enter to continue')
    elif selection == '2':
        print(grocery_list)
        input('Enter to continue')
    elif selection == '3':
        print(f'ITEM COUNT: {len(grocery_list)}')
        input('Enter to continue')
    elif selection == '4':
        print(grocery_list[0])
        input('Enter to continue')
    elif selection == '5':
        print(grocery_list[-1])
        input('Enter to continue')
    elif selection == '6':
        grocery_list = []
        input('Enter to continue')
    elif selection == '7':
        print('Exiting')
        break
    else:
        print('Please enter a valid option')