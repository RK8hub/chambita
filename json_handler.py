from dataclasses import dataclass
import json








def crear_json(nombre:str, informacion):
    with open(nombre,'w',encoding='utf-8') as archivo:
        json.dump(informacion, archivo, indent=4, ensure_ascii=False)
        
def leer_json(nombre):
    with open(nombre,'r',encoding='utf-8') as inforacion:
        return json.load(inforacion)

def agregar_json(nombre, informacion):
    try:
        
        with open(nombre, 'r', encoding='utf-8') as archivo:
            json_informacion = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        
        json_informacion = {}

    
    json_informacion.append(informacion)

    
    with open(nombre, 'w', encoding='utf-8') as archivo:
        json.dump(json_informacion, archivo, indent=4, ensure_ascii=False)
