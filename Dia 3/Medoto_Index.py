mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5, 12)

print(resultado)

palabra = "ordenador"
resultado = palabra[5]

print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado2 = frase.index("práctica")

print(resultado2)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado3 = frase.rindex("práctica")
print(resultado3)