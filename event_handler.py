# ---Esto es para Debug, Debe ser eliminado al finalizar---
from pprint import pprint

from json_handler import Json, leer
from data_frame_handler import exportar
from baki import *


internal_data = cargar_objetos('data/objetos')
simple_data = {i.json['informacion']['operador'].upper(): i.json['id'] for i in internal_data}


def validacion_de_inicial():
    try:
        with open('data/History.log','r',encoding='utf-8') as history:
            return False
    except:
        with open('data/History.log','w',encoding='utf-8')as new_history:
            return True

def obtener_id(operador):
    resultados = {}
    nombres = list(simple_data.keys())
    for i in nombres:
        if operador.upper() in i:
            resultados[i] = simple_data[i]
    if len(resultados) == 0:
        return ["Sin resultados"]
    return resultados

def obtener_informacion(ID):
    for i in internal_data:
        if i.json['id'] == ID:
            return i.json

dict_json = [_.json for _ in internal_data]
pprint(dict_json)
exportar(dict_json,'prueba.html')