import xml.etree.ElementTree as ET

# Supongamos que tenemos el siguiente fragmento de XML
import xml.etree.ElementTree as ET

# Supongamos que tenemos el siguiente fragmento de XML
xml_string = """
<frutas>
    <fruta>
        <nombre>Manzana</nombre>
        <color>Rojo</color>
        <precio>Rojo</precio>
    </fruta>
    <fruta>
        <nombre>Plátano</nombre>
        <color>Amarillo</color>
        <precio>Rojo</precio>
    </fruta>
    <fruta>
        <nombre>Uva</nombre>
        <color>Morado</color>
        <precio>Rojo</precio>
    </fruta>
    <fruta>
        <nombre>Sandia</nombre>
        <color>Rojo</color>
        <precio>Rojo</precio>
    </fruta>
    <fruta>
        <nombre>Pera</nombre>
        <color>Verde</color>
        <precio>Rojo</precio>
    </fruta>
</frutas>
"""

# Se parsea el XML
root = ET.fromstring(xml_string)

# Función para buscar una fruta por nombre
def buscar_fruta_por_nombre(nombre):
    for fruta in root.findall(".//fruta[nombre='" + nombre + "']"):
        color = fruta.find('color').text
        precio = fruta.find('precio').text
        print(f"{nombre} es de color {color} y tiene un precio de {precio}.")

# Bucle interactivo
while True:
    # Solicitar entrada del usuario
    consulta = input("Ingrese la fruta que desea o 'salir' para terminar la búsqueda: ")

    # Verificar si el usuario desea salir
    if consulta.lower() == "salir":
        break

    # Realizar la consulta
    buscar_fruta_por_nombre(consulta)