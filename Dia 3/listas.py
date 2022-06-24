# otra_lista = ['hola', 55, 6.1]
mi_lista = ['a', 'b', 'c']
resultado = len(mi_lista)
# resultado = mi_lista[0:]

mi_lista2=['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3[0]= 'alfa'

mi_lista3.append('g')
# mi_lista3.pop()
# mi_lista3.pop(0)

delete = mi_lista3.pop(0)

# print(mi_lista3)
# print(delete)


lista= ['g','o','b', 'm', 'c']

#Ordenar alfabeticamente
lista.sort()

#No se puede almacenar en una variable un metodo de una lista
miNuevaLista= lista.sort()

#Como resultado da un None


#Metodo Reverse
lista.reverse()

print(lista)