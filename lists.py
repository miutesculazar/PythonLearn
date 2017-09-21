l = []

print('type:', type(l))



l.append('abc')
l.append([1, 2])
l.append(6)
l.append(5)
l.extend([1, 4, 5, 9])

print('lista:', l)

print('marime:', len(l))

print('elementul 2:', l[1])
print('de la el4 la sfarsit:', l[3:])
print('de la el4 la sfarsit:', l[3:len(l)+2])
print('ultimul element:', l[-1])
print('ultimele 2 elemente:', l[-2:])
print('elementele 3 si 4:', l[2:4])


cuvant = 'gigi are prune'

print('ultimul cuvant:', cuvant[-5:])
print('split dupa spatiu:', cuvant.split(' '))

print('indexul primei aparitii in lista a elementului:', l.index(5))

#print all elements of the list
for item in l:
    print(item)

#print the type of the element beautifully
for item in l:
    tipul = type(item)
    print(f'{tipul.__name__}')


if 'a' == '6':
    print('a')
elif not 5 in l:
    print('b')
else:
    print('go home')


lista_noua = []
for item in l:
    if type(item) == int:
        lista_noua.append(item)
print('lista noua:', lista_noua)


# printare lista in ordine inversa
# varianta simpla
lista_noua.reverse()
print('lista inversa:', lista_noua)

#varianta complicata
lista_foarte_noua = lista_noua[::-1]
print(lista_foarte_noua)

while 5 in lista_foarte_noua:
    lista_foarte_noua.pop()
    print(lista_foarte_noua)


#list comprehension
new_list = []
for i in l:
    if type(i) == int:
        new_list.append(i)

#easier method for above
int_list = [i for i in l if type(i) == int]

