# Una lista es lo que llamamos array en otros lenguajes
x = ["one", "two"]

print(x)
print(type(x))

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

lista_cursos[4] = 'Rust'

print(lista_cursos)

# Sublistas

sub_lista = lista_cursos[0:3]
print(sub_lista)
sub_lista = lista_cursos[2:]
print(f"[2:] {sub_lista}")
sub_lista = lista_cursos[:3]
print(f"[:3] {sub_lista}")

sub_lista = lista_cursos[1:5:2]
print(f"[1:5:2] {sub_lista}")

sub_lista = lista_cursos[::2]
print(f"[::2] {sub_lista}")


lista_cursos.append("JavaScript")
lista_cursos.insert(1, "C")
print(lista_cursos)

nueva_lista = ["Docker", "C++", "MongoDB"]
lista_cursos.extend(nueva_lista)
print(lista_cursos)

lista_cursos.remove("MongoDB")
print(lista_cursos);
