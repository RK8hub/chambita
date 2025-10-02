from excel_manage import inyectar
from template import Template, Ram, Almacenamiento
from pprint import pprint
from json_handler import Json
import baki

# principal
data = Json('data/','database')
objt_list = []
data_list = inyectar()

#recorrer
for i in data_list:
    objt_list.append(Template(*i,'managua'))

for i in objt_list:
    data.agregar_diccionario(i.json)
        
baki.guardar_objetos('objetos',objt_list)