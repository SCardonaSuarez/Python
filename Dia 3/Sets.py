#Lo mas importante es que admiten los elemento unicos y no acepta duplicados
#Tampoco van en indices
#Tampoco puede incluir listas y diccionarios

# print(otro_set)
# otro_set = {1,2,3}

mi_set = set([1,2,3,4,5])
# print(type(mi_set))
print(mi_set)


my_set= {1,2,3,4,5}
my_set = set((1,2,3,4,(1,2,3),5,6))
print(my_set)
print(type(my_set))

print(len(my_set))
print(2 in my_set)


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#Agregar un elemento/valor al set
s1.add(4)
print(s1)

#Eliminar
s1.remove(3)
print(s1)

#Discart
s1.discard(6)
print(s1)

#metodo que eliminar al asar
sorteo = s1.pop()

print(sorteo)

#Clear vacea todo el set 
s1.clear()
print(s1)
