# def nume(param):
#     #actiuni
#     pass
#     return #optional


# def suma(a=1, b=3): # =x this the default value, if none is sent this will be taken
#     s = a + b
#     return s
#
# s = suma([1, 2], [2, 5])
# s = suma(b=4) # will add 1 (default for a) + 4
#
# print(s)


"""
prima functie: Citim 2 numere de la tastatura si returnam int

functia 2: Comparam inputs de la fct1
Daca nr 1 >= nr 2 => True altfel false

functia 3: cu output de la fct2:
    Daca e TRUE => Ccerem de la tastatura alt numar

functia 4:
    DAca e False => sa il inlocuiasca primul element cu primul numar impar mai mic decat el

"""


def new_input(text):
    return int(input(text))


def read_input():
    first_number = new_input('Primul numar este: ')
    second_number = new_input('Al doilea numar este: ')
    return first_number, second_number


def compare(value1, value2):
    if value1 >= value2:
        return True
    else:
        return False

numar1, numar2 = read_input()

if compare(numar1, numar2):
    numar1 = new_input('Avem nevoie de un nou numar: ')
else:
    if numar1%2 == 0:
        numar1 = numar1 - 1
    else:
        numar1 = numar1 - 2

print(numar1, numar2)




