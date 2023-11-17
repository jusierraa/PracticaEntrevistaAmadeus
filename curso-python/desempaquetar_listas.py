numeros = [1, 2, 3]
primero, segundo, tercero = numeros
primero, *otros, ultimo = numeros ##coger el primero y el ultimo

#######iterar listas
numeros = [1, 2, 3, 4]
for indice, numeros in enumerate(numeros): ##enumera la lista
    print(numeros, indice)
numeros.index("2") ###buscar posición del arreglo

print(numeros.count("2"))
if "2" in numeros:
    print(numeros.index("2"))
 


