#exercise 1
print('witaj w naszym kalkulatorzę')
while True:
    x = (input('podaj pierwszą liczbę: '))
    y = (input('podaj drugą liczbę: '))


    if x == '' or y == '':
        continue

    print('Jakie działanie chcesz wykonać wybierz odpowiedni numer')
    print(' 1 /\n 2 *\n 3 +\n 4 -\n 5 **\n 6 Wyjscie z programu.')


    option = int(input())    # tu też warto coś zrobić  z if i or i złamać program
    x = float(x)
    y = float(y)

    if option == 1:

        try:
            print(x/y)
        except ValueError:
            print('Tylko liczby!')
        except ZeroDivisionError:
            print('Przez zero serio!!!!!!!!!!!')

    elif option == 2:

        try:
            print(x*y)
        except ValueError:
            print('Tylko liczby!')


    elif option == 3:
        try:

            print(x + y)
        except ValueError:
            print('Tylko liczby!')

    elif option == 4:
        try:

            print(x - y)
        except ValueError:
            print('Tylko liczby!')

    elif option == 5:
        try:

            print(x**y)
        except ValueError:
            print('Blad: Tylko liczby. Pamietaj nie wolno definiowac potegi w zakresie liczb wymiernych dla liczb ujemnych. ')

    elif option == 6:
        break



#exercise 2
import random
print('\n')
a= input('Jaka ma byc wartosc minimalna dla listy? ')
b = input('Jaka ma byc wartosc maksymalna dla listy? ')
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
print('Zmieniony zostal element, ktory znajduje sie pod indexem nr', list1.index(int(NewIndeks/1000)))

print('\n')

#exercise 3

Plik = open('ListaZakupow.txt', 'w')
Plik.write('Lista zakupow: ')
Plik.close()
variable = ' '
def option1(variable):
    print("Wybrales opcje dodania produktu do listy zakupów.\n")

    while variable == '1':
        file = open('ListaZakupow.txt', 'a')
        lista = []
        product = input('Wpisz produkt: ')
        lista.append(product)
        for i in lista:
            file.write('\n')
            file.write(i)

        what_next = input('Czy chcesz dodac kolejny produkt? t/n?')
        if what_next == 't':
            variable = '1'
            continue
        elif (what_next == 'n'):
            break
            variable = ' '
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break
            variable = ' '
        file.close()

def option2(variable):
    print("Wybrales opcje usowania produktów z listy.\n")

    while variable == '2':
        file = open('ListaZakupow.txt', 'r')
        lista = []
        for i in file.readlines():
            lista.append(i)
        file.close()

        delete = input('Wybierz jaki produkt chcesz usunac: ')
        file = open('ListaZakupow.txt', 'w')
        value = list(map(lambda x: x.rstrip('\n'), lista))
        value.remove(delete)

        for i in value:
            file.write(i)
            file.write('\n')
        file.close()

        what_next = input('Czy chcesz usunąć jeszcze jakiś produkt z listy zakupów? t/n?')
        if what_next == 't':
            variable = '2'
            continue
        elif what_next == 'n':
            variable == ' '
            break
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break
            variable = ''


def option3(variable):
    print("Wybrales opcje pokazania listy zakupów.\n")
    while variable == '3':
        line = open('ListaZakupow.txt')
        for i in line.readlines():
            print(i)
        line.close()
        print('\n')

        what_next = input('Czy chcesz powrocic do menu? t/n?')
        if what_next == 't':
            variable = ' '
            break
        elif what_next == 'n':
            variable == '3'
            continue
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break
            variable = ''

def option4(variable):
    while variable == '4':
        print("Wybrales opcje czyszczenia listy! \n")
        file = open('ListaZakupow.txt', 'w' )
        file.write('Lista zakupów: ')
        file.close()
        what_next = input('Lista zostala wyczyszczona czy chcesz powrocic do menu? t/n?')
        if what_next == 't':
            variable = ' '
            break
        elif what_next == 'n':
            variable == '3'
            continue
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break
            variable = ''


while variable != 'Stop':
    print('Witaj w programie lista zakupow! \n')
    print('========== Menu ==========')
    print('1. Dodaj produkt do kupienia.\n2. Usun produkt.\n3. Wyswietl liste zakupow.\n4. Wyczysc liste zakupow.')
    print('Jeśli chcesz wyjsc z programu wpisz "Stop"')
    variable = input(f'Wybierz opcję i naciśnij ENTER: ')
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
    if variable not in ['1', '2', '3', '4']:
        print('BLAD')
        continue