import xml.etree.cElementTree as ET


ruta = "C:\\Users\\jcsie\\OneDrive\\Documents\\Elementos importantes para programar\\curso-python\\"

root = ET.Element("root")   ##Nodo principal
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "nodo1", name = "nodo").text = "texto nodo1"   ###Atributos
ET.SubElement(doc, "nodo2", atributo = "manzana").text ="texto nodo2"

archivo = ET.ElementTree(root)
archivo.write(ruta + "EjemplocrearXML.xml")
