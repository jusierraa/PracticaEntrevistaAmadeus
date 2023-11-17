 #!/bin/bash
#Author Juan Camilo Sierra
# Este es un escript de funciones Shell

echo "-----------------------Función hola_mundo"
hola_mundo (){
	echo "Hola mundo"
}
hola_mundo

echo "-------------------------------Funcion parametros"
parametros (){
	echo "Hola soy $1 y me gusta $2"

}

echo "digite su nombre y canal"
read nombre
echo "Digite canal"
read canal

parametros $nombre $canal
hola_mundo
