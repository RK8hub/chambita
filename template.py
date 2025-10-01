from dataclasses import dataclass, field, asdict, fields
import secrets

@dataclass
class Componente:
    tipo: str
    capacidad: str
    def __post_init__(self):
      for f in fields(self):  # recorre todos los atributos del dataclass
            valor = getattr(self, f.name)
            if isinstance(valor, str) and valor.strip() == "":
                raise ValueError(f"El campo '{f.name}' está vacío")
      
class Almacenamiento(Componente):pass
    
class Ram(Componente):pass


@dataclass
class Template:
    area: str
    operador: str
    equipo: str
    modelo: str
    numero_de_serie: str
    codigo_de_fabricacion: str
    departamento: str
    ID: str = field(init=False,default=None)
    
    departamentos_code = {
    "BOACO": "BO",
    "CARAZO": "CA",
    "CHINANDEGA": "CH",
    "CHONTALES": "CN",
    "ESTELI": "ES",
    "GRANADA": "GR",
    "JINOTEGA": "JI",
    "LEON": "LE",
    "MADRIZ": "MA",
    "MANAGUA": "MN",
    "MASAYA": "MS",
    "MATAGALPA": "MT",
    "NUEVA SEGOVIA": "NS",
    "RIO SAN JUAN": "SJ",
    "RIVAS": "RI",
    "REGION AUTONOMA DE LA COSTA CARIBE NORTE": "RACN",
    "REGION AUTONOMA DE LA COSTA CARIBE SUR": "RACS"
    }
    
    def __post_init__(self):
      for f in fields(self):  # recorre todos los atributos del dataclass
            valor = getattr(self, f.name)
            if isinstance(valor, str) and valor.strip() == "":
                raise ValueError(f"El campo '{f.name}' está vacío")
      self.departamento = self.departamento.upper()
      self.ID = self.determinar_ID()
      self.json = {
          
          "id": f"{self.ID}",
          "informacion": {
            "area": f"{self.area}",
            "operador": f"{self.operador}",
            "equipo": f"{self.equipo}",
            "modelo": f"{self.modelo}",
            "numero_de_serie": f"{self.numero_de_serie}",
            "codigo_de_fabricacion": f"{self.codigo_de_fabricacion}",
            },
          
            }
      self.json["intervenciones"] = {}
    
    def determinar_ID(self):
      if self.ID  == None:
          salt = ''.join(str(secrets.randbelow(10)) for _ in range(6))
          constructo = f"{self.departamentos_code[self.departamento]}-{salt}"
          return constructo
        
    def ingresar_especificaciones(self,procesador: str,sistema_operativo: str,ram: list,almacenamiento: list,):
      for f in fields(self):  # recorre todos los atributos del dataclass
            valor = getattr(self, f.name)
            if isinstance(valor, str) and valor.strip() == "":
                raise ValueError(f"El campo '{f.name}' está vacío")
      self.json["especificaciones"] = {
        
        "procesador": f'{procesador}',
        "sistema_operativo": f'{sistema_operativo}',
        "ram": [asdict(r) for r in ram],
        "almacenamiento": [asdict(a) for a in almacenamiento]

      }
    def ingresar_intervencion(self,fecha:str, razon: str):
      for f in fields(self):  # recorre todos los atributos del dataclass
            valor = getattr(self, f.name)
            if isinstance(valor, str) and valor.strip() == "":
                raise ValueError(f"El campo '{f.name}' está vacío")
      self.json["intervenciones"][str(len(self.json["intervenciones"]) +1)] = {"fecha": fecha, "razon": razon}