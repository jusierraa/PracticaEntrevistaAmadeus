import json

"""" """

# json_str = '{"nombre": "Oscar","edad":28, "pais":"Colombia" }' 

# python_dict = json.loads(json_str)  ### convertir a diccionario
# print(python_dict)
# print(python_dict['nombre'])        ###Buscar dato


data = {
    "Ingeniero" : "Juan Sierra",
    "edad" : "27",
    "universidad" : "Nacional",
    "cursos" : ["PHP", "python", "Java", "SQL" ]
}

# json_data=json.dumps(data, indent=4,separators=(", ", " : "), sort_keys=True)   ######Convertir a str
# print(json_data)   

json_data = json.JSONEncoder().encode({"lenguajes":["python,jvs"]})


python:dict = json.JSONDecoder().decode(json_data)


# json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
# json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

# Diccionarios (dict)
# Listas y tuplas (list, tuple)
# Cadenas (str en Python 3, unicode en Python 2)
# Números (int, float)
# True, False, y None