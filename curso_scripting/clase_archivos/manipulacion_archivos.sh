
#!/bin/bash
#AUTHOR Juan camilo Sierra



#Este script enseña a manipular archivos

input_type=""
input_name=""
input_text=""

echo "Desear generar  un directorio(1) o archivo (2)?: "
read input_type

if (($input_type == 1)); then
	read -p "Ingrese el nombre del 



directorio: " input_name
	mkdir -m  $input_name
	chmod +x $input_name
fi

if(($input_type == 2)); then
	echo "Ingrese nombre del archivo: "
	read input_name
	touch -m 777 $input_name
	echo "Ingrese un texto que desea tener en el archivo $input_name"
	read input_text
	echo $input_text >> $input_name
	echo "contenido del archivo: "
	cat $input_name
	chmod +x $input_name
fi
