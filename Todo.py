first = ('random')
data = []

def MENU():
    print('MENU:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. The item has been added')
    print('4. Exit')



while first != '4':
    
    MENU()
    first = input('ENTER YOUR CHOICE: ')

    if first == '1':
        item = input('Enter the item to be added: ')
        data.append(item)
        print('Added item', item)
    elif first == '2':
        item = input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item', item)
        else:
            print('Item does not exist')
    elif first == '3':
        print('TO DO LIST')
        for item in data:
            print(item)
    elif first == '4':
        print ('Goodbye!!')
    else:
        print ('Enter from these choices: 1,2,3,4')
