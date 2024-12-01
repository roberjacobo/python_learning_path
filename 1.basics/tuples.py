tupla = ('Roberto', 24, True, [1, 2, 3], (4, 5, 6))
print(tupla)

print(tupla[0])


# Descomprimir
# * -> Lista
# _ -> Omitir valor(es)

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, dos, tres, cuatro, *resto_valores = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)


# *_ -> Va a ignorar los valores que abarque
uno, dos, tres, cuatro, *_, diez = numeros


print(uno)
print(dos)
print(tres)
print(cuatro)
print(diez)