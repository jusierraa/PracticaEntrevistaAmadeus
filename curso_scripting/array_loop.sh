#!/bin/bash
#AUTHOR: Juan  Sierra
#Arreglos-Iteración

numeros=(1 2 3)
nombres=("Juan Sierra" "Sonia Alean" "Diego Sierra" Alejandro)
rangos=({0..4} {A..Z})

echo "Arreglo de números: ${numeros[*]}"
echo "Arreglo de números: ${nombres[*]}"
echo "Arreglo de números: ${rangos[*]}"

echo "----Numero de elementos en el arreglo -----"

echo "Tamaño Arreglo de números: ${#numeros[*]}"
echo "Tamaño Arreglo de números: ${#nombres[*]}"
echo "Tamaño Arreglo de números: ${#rangos[*]}"

echo "----Manipular arreglos-----"

unset numeros[0]
echo "Arreglo de números: ${numeros[*]}"
numeros[0]=1
echo "Arreglo de números: ${numeros[*]}"

echo "----Iteración----"

for num in ${numeros[*]}
do
	echo "Numero: $num"
done

echo "----Iteraciones 2----"

for ((i=0; i<${#numeros[*]}; i++))
do
	echo "Numero ${numeros[i]}"
done

echo "------------------Ejercicio multiplica todos los numeros de un arreglo por el que digamos-------------------------------"

echo "Ingresa un número"
read numero

arreglo=()

for ((i=1; i<=numero; i++)); do
	arreglo+=($i)
done

resultado=0

for((i = 0; i < ${#arreglo[*]}; i++)); do
	resultado=$((numero * arreglo[i]))
	echo "El resultado de la multiplicaión entre $((arreglo[i])) y $numero es:  $resultado"

done


echo "-------------------------------------ejemplo 2 suma de todos los numeros en el arreglo-------------------------------"


echo "Ingresa un numero: "
read numero

arreglo=()

for((i=1;i<=numero; i++ )) do
	arreglo+=($i)
done

echo "${arreglo[*]}"
resultado=0

for((i = 0; i < ${#arreglo[*]}-1; i++)) do
	resultado=$((resultado + arreglo[i]))
done
resultado=$((resultado + arreglo[i]))
echo "resultado= $resultado"



