from template import Template, Ram, Almacenamiento
from pprint import pprint
from json_handler import *

json_padre= crear_json("data.json",[])

prueba = Template('informatica','Raul Emmanuel Aguilar','lenovo G50','80QQ','123456','21383718','Chontales')
prueba.ingresar_especificaciones('intel CoreI5','Archcraft',[Ram('DDR4','8GB')],[Almacenamiento('HHD','120GB')])
prueba1 = Template('informatica','Leonardo Perez Alvarado','lenovo G50','80QQ','123456','21383718','managua')
prueba1.ingresar_especificaciones('intel CoreI5','Archcraft',[Ram('DDR4','8GB')],[Almacenamiento('HHD','120GB')])


agregar_json('data.json',prueba.json)

agregar_json('data.json',prueba1.json)

json_back = leer_json('data.json')

pprint(json_back[1])
