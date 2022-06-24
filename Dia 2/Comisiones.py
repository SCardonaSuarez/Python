name = input("Dime tu nombre: ")
sell = float(input("Cuanto fue las ventas?")) #13/100
sellPorcent = round((sell * 13) / 100, 2)
print(f" {name} ventas: ${sellPorcent}")
