#1. Decirle al usuario que ingrese un texto
#2. Ingrese 3 letras a su eleccion
#3. como resultado saber cuantas veces aparece la palabra en el texto se debe
#almacenar en un diccionario
#4  Cual es la primer letra y cual es la ultima del texto
#5 Invertir el orden
#6 aparece python en el texto? booleanos

# text = input("Introduce un texto en cualquier idioma: ").lower()
# print("Introduce 3 letras: ")
# letter1 = input("Digita la 1 letra: ")
# letter2 = input("Digita la 2 letra: ")
# letter3 = input("Digita la 3 letras: ")
#
# letters = {'1': letter1, '2': letter2, '3': letter3}
#
# search_letters = text

text = input("Introduce un texto en cualquier idioma: ").lower()
letras = []
text = text.lower()

letras.append(input("Digita la 1 letra: ").lower() )
letras.append(input("Digita la 2 letra: ").lower() )
letras.append(input("Digita la 3 letra: ").lower() )

print("\n")
print("Cantidad de letras")

cantidad_letras1 = text.count(letras[0])
cantidad_letras2 = text.count(letras[1])
cantidad_letras3 = text.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")


print("\n")
print("Cantidad de Palabras")

palabras = text.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto.")

print("\n")
print("Letras de inicio y de fin")
letras_inicio = text[0]
letra_final = text[-1]

print(f"La letra incial es '{letras_inicio}' y la letra final es: '{letra_final}'")


print("\n")
print("Texto Invertido")

palabras.reverse()
texto_invertido = ' '.join(palabras)

print(f"Si ordenamos tu texto al revez tu texto: '{texto_invertido}'")

print("\n")
print("Buscado la palabra Python")

buscar_python = 'python' in text
dic = {True: "si", False: "no"}

print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")