#Los tubples son inmutables

mi_tuple = (1,2,(10,20),4)
# t = (5,5.6, 'ff')

#No se puede cambiar sus valores
# mi_tuple[0]= 5

mi_tuple = list(mi_tuple)
mi_tuple = tuple(mi_tuple)

t = (1,2,3,1)
# x,y,z = t


print((t.count(1)))
print(t.index(2))
# print(len(t))
# print(mi_tuple[2][0])

