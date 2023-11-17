nota = input("ingresa la nota: ")
nota1 = int (nota)
if nota1 <= 4:
    print("el estudiante es destacado")
elif nota1 < 3:
    print("perdió")
else: 
    print("pasó la materia")