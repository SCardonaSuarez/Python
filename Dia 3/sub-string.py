texto = "ABCDEFGHIJKALMN"
fragmento1 = texto[2:10 ]

fragmento2 = texto[2:10:2 ]

fragmento3 = texto[::2 ]

fragmento4 = texto[::-1 ]


print(fragmento1)
print(fragmento2)
print(fragmento3)
print(fragmento4)


frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmentos = frase[8::3]
print(fragmentos)