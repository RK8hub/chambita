from pprint import pprint
import json


# Abrir el archivo en modo lectura
with open('ejemplo.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)  # Carga el contenido JSON en un diccionario de Python

# Ahora 'datos' es un diccionario o lista según la estructura del JSON
pprint(datos[1])

