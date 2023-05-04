#exercise 1
while True:
    print('Welcome in the calculator app!')
    print('What calculation would you like to perform? Select number:')
    print(' 1 /\n 2 *\n 3 +\n 4 -\n 5 **\n 6 Exit.')

    option = int(input('Calculation number: '))  

    if option == 6:
        break

    x = (input('First nuber: '))
    y = (input('Second number: '))

    if x == '' or y == '':
        continue

    x = float(x)
    y = float(y)

    if option == 1:

        try:
            print(x/y)
        except ValueError:
            print('Only numbers!')
        except ZeroDivisionError:
            print('You can t divide by zero!')

    elif option == 2:

        try:
            print(x*y)
        except ValueError:
            print('Only numbers!')


    elif option == 3:
        try:

            print(x + y)
        except ValueError:
            print('Only numbers!')

    elif option == 4:
        try:

            print(x - y)
        except ValueError:
            print('Only numbers!')

    elif option == 5:
        try:

            print(x**y)
        except ValueError:
            print('Error: Only numbers. Remember it is not allowed to define powers in terms of measurable numbers for negative numbers. ')


#exercise 2
import random
print('\n')
a= input('What should be the minimum value for the list? ')
b = input('What should be the maximum value for the list? ')
a = int(a)
b = int(b)
list1 = list(range(a,b))
print(list1)

list2 = list1.copy()
losowy = random.randint(a,b-1)

indeks = list2.index(losowy)
NewIndeks = list2[indeks] * 1000
list2[indeks] = NewIndeks
print(list2)
print('Changed was the element that is located under the index no. ', list1.index(int(NewIndeks/1000)))

print('\n')

#exercise 3

Plik = open('ShoppingList.txt', 'w')
Plik.write('Shopping list: ')
Plik.close()
variable = ' '
def option1(variable):
    print('You have chosen the option to add the product to your shopping list.\n')

    while variable == '1':
        file = open('ShoppingList.txt', 'a')
        lista = []
        product = input('Add product: ')
        lista.append(product)
        for i in lista:
            file.write('\n')
            file.write(i)

        what_next = input('Would you like to add another product? /n?')
        if what_next == 't':
            variable = '1'
            continue
        elif (what_next == 'n'):
            break
            variable = ' '
        else:
            print(f'The specified value {what_next} is invalid. You are taken to the menu.')
            break
            variable = ' '
        file.close()

def option2(variable):
    print("You have chosen the option to delete products from the list.\n")

    while variable == '2':
        file = open('ShoppingList.txt', 'r')
        lista = []
        for i in file.readlines():
            lista.append(i)
        file.close()

        delete = input('Select which product you want to remove: ')
        file = open('ShoppingList.txt', 'w')
        value = list(map(lambda x: x.rstrip('\n'), lista))
        value.remove(delete)

        for i in value:
            file.write(i)
            file.write('\n')
        file.close()

        what_next = input('Do you want to remove any more products from your shopping list? t/n?')
        if what_next == 't':
            variable = '2'
            continue
        elif what_next == 'n':
            variable == ' '
            break
        else:
            print(f'The specified value {what_next} is invalid. You are taken to the menu.')
            break
            variable = ''


def option3(variable):
    print("You chose the option to show a shopping list.\n")
    while variable == '3':
        line = open('ShoppingList.txt')
        for i in line.readlines():
            print(i)
        line.close()
        print('\n')

        what_next = input('Do you want to return to the menu? t/n?')
        if what_next == 't':
            variable = ' '
            break
        elif what_next == 'n':
            variable == '3'
            continue
        else:
            print(f'The specified value {what_next} is invalid. You are taken to the menu.')
            break
            variable = ''

def option4(variable):
    while variable == '4':
        print("You have chosen the option to clear the list! \n")
        file = open('ShoppingList.txt', 'w' )
        file.write('Shopping list: ')
        file.close()
        what_next = input('The list has been cleared or you want to return to the menu? t/n?')
        if what_next == 't':
            variable = ' '
            break
        elif what_next == 'n':
            variable == '3'
            continue
        else:
            print(f'The specified value {what_next} is invalid. You are taken to the menu.')
            break
            variable = ''


while variable.lower() != 'stop':
    print('Welcome to the shopping list program! \n')
    print('========== Menu ==========')
    print('1. Add a product to buy.\n2. Delete product.\n3. Display the shopping list.\n4. Clear the shopping list.')
    print('If you want to exit the program type "Stop"')
    variable = input(f'Select an option and press ENTER: ')
    if variable == '1':
        print()
        option1('1')
    if variable == '2':
        print()
        option2('2')
    if variable == '3':
        print()
        option3('3')
    if variable == '4':
        print()
        option4('4')
    if variable.lower() == 'stop':
        print('Thank you!')
        break
    if variable not in ['1', '2', '3', '4']:
        print('Error')
        continue