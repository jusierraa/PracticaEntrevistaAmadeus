
#########################Escribe uno a uno el arreglo que se tiene#################3
lenguajes = ["java", "python", "linux"]
for num  in lenguajes:
    print(num)

for lengua in lenguajes:
    print(lengua)
    
######################################Saber el largo de una cadena de texto#######
def largo(texto):  
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado
l = largo("Hola mundo")
print(l)
###################################### Palindromo ####################################
def no_space(texto): ####Quitar espacios de un texto
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto
def reverse(texto): ########### voltear un texto
    texto_al_reves = ""
    for char in texto:
        texto_al_reves= char + texto_al_reves
    return (texto_al_reves)    
def palindromo(texto):
    texto = no_space(texto).lower()
    texto_al_reves = reverse(texto).lower()
    palindromos = 0
    for char in texto_al_reves:
        if texto_al_reves == texto:
                palindromos += 1
    if palindromos  == len(texto):
        print("Es palindromo")
    else:
        print("No es palindromo")

palindromo("amo la palona")   
palindromo("Ama")     
################


