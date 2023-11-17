# !/bin/bash
# AUTHOR Juan Camilo Sierra
#Ejemplos de variables y parámetros dinamicos 


nombre=$1
apellido=$2
ubicacion=$(pwd)
echo "Mi nombre es $nombre $apellido"
echo $ubicacion
pwd
echo "La cantidad de parametros enviados es $#"
echo "Los parametros enviados por el usuario son $*"
