from template import Template, Ram, Almacenamiento
from pprint import pprint
from json_handler import Json

json_padre= Json('','data')

prueba = Template('informatica','Raul Emmanuel Aguilar','lenovo G50','80QQ','123456','21383718','Chontales')
prueba.ingresar_especificaciones('intel CoreI5','Archcraft',[Ram('DDR4','8GB')],[Almacenamiento('HHD','120GB')])
prueba1 = Template('informatica','Leonardo Perez Alvarado','lenovo G50','80QQ','123456','21383718','managua')
prueba1.ingresar_especificaciones('intel CoreI5','Archcraft',[Ram('DDR4','8GB')],[Almacenamiento('HHD','120GB')])


json_padre.agregar_diccionario(prueba.json)

json_padre.agregar_diccionario(prueba1.json)

json_back= Json('',"Back_up")

json_back.clonar(json_padre)

pprint(json_back.leer()[0])