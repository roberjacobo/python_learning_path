# Hay tres tipos de colecciones en python
#
# List
# Tuples
# Dictionaries

# List es el tipo de colección más flexible conocido como array en otros lenguajes

myList = ['mouse', 'keyboard', 'pc']
print('La lista tiene ', len(myList), ' elementos')
print(myList)
print('El primer elemento de la lista es: ', myList[0])
otherList = ['speakers', 'monitor']

twoLists = myList + otherList

print(twoLists)

print(twoLists + ['desktop'])
twoLists[3] = 'headset'
print(twoLists + ['desktop'])
print('Usando del en el primer elemento')
del twoLists[0]

print(twoLists + ['desktop'])
listThree = twoLists + ['desktop', ['mouse']]
print('listThree: ', listThree)