from dataclasses import dataclass
import json

@dataclass
class Json:
    ruta: str
    nombre: str
    
    def __post_init__(self):
        self.entity = f'{self.ruta}{self.nombre}.json'
        with open(self.entity,'w',encoding='utf-8') as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)
            
    def leer(self):
        with open(self.entity,'r',encoding='utf-8') as inforacion:
            return json.load(inforacion)
    def agregar_diccionario(self, informacion):
        try:
            
            with open(self.entity, 'r', encoding='utf-8') as archivo:
                json_informacion = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            
            json_informacion = {}

        json_informacion.append(informacion)

        
        with open(self.entity, 'w', encoding='utf-8') as archivo:
            json.dump(json_informacion, archivo, indent=4, ensure_ascii=False)
            
    def clonar(self, other):
        with open(other.entity, 'r', encoding='utf-8') as f:
            informacion = json.load(f)

        with open(self.entity, 'w', encoding='utf-8') as f:
            json.dump(informacion, f, indent=4, ensure_ascii=False)
