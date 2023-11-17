#!/bin/bash
#AUTHOR Juan Camilo Sierra
#Este es un script para lectura de archivos

input_name=$1
echo "-----------------------------Lectura de archivos con CAT------------------------------------"
cat $input_name
echo "-------------------------------Lectura Linea por linea-----------------------------------"
echo "IFS (INTERNAL FIELD SEPARATOR), PARA LEEER LINEA POR LINEA"

while IFS= read line; do
	echo "---$line---"
done < "$input_name"
