from dataclasses import dataclass, field, asdict
from pprint import pprint
import secrets

@dataclass
class Componente:
    tipo: str
    capacidad: str
    def __post_init__(self):
      if self.tipo == '' or self.capacidad =='':
        raise ValueError('varible vacia')
      
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
    "ESTELÍ": "ES",
    "GRANADA": "GR",
    "JINOTEGA": "JI",
    "LEÓN": "LE",
    "MADRIZ": "MA",
    "MANAGUA": "MN",
    "MASAYA": "MS",
    "MATAGALPA": "MT",
    "NUEVA SEGOVIA": "NS",
    "RÍO SAN JUAN": "SJ",
    "RIVAS": "RI",
    "REGIÓN AUTÓNOMA DE LA COSTA CARIBE NORTE": "RACN",
    "REGIÓN AUTÓNOMA DE LA COSTA CARIBE SUR": "RACS"
    }
    
    def __post_init__(self):
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
    
    def determinar_ID(self):
      if self.ID  == None:
          salt = ''.join(str(secrets.randbelow(10)) for _ in range(6))
          constructo = f"{self.departamentos_code[self.departamento]}-{salt}"
          return constructo
        
    def ingresar_especificaciones(self,procesador: str,sistema_operativo: str,ram: list,almacenamiento: list,):
      self.json["especificaciones"] = {
        
        "procesador": f'{procesador}',
        "sistema_operativo": f'{sistema_operativo}',
        "ram": [asdict(r) for r in ram],
        "almacenamiento": [asdict(a) for a in almacenamiento]
        
        
      }
      
    
Ejemplo = Template("Datos Y Noc","Franklin Perez",'ideapad 100-151BQ','80QQ','PFOESUE8','PF9XB5B29005','Managua')
Ejemplo.ingresar_especificaciones('intel core I5','Windows vista',[Ram('DDR4L','8GB')],[Almacenamiento("HDD","450GB")])
pprint(Ejemplo.json["especificaciones"])

datos={
    "id": "EQ-0MN",
    "informacion": {
      "modelo": "Dell Latitude 5420",
      "numero_de_serie": "DL5420-1234",
      "operador": "Juan Pérez",
      "ubicacion": "Oficina Principal"
    },
    "especificaciones": {
      "almacenamiento": [
        {"tipo": "SSD", "cantidad": "512GB"},
        {"tipo": "HDD", "cantidad": "1TB"}
      ],
      "procesador": "Intel i7-1185G7",
      "memoria": [
        {"tipo": "DDR4", "cantidad": "16GB"}
      ],
      "sistema": "Windows 11 Pro"
    },
    "intervenciones": {
      "1": {"fecha": "2025-07-15", "razon": "Cambio de disco SSD"},
      "2": {"fecha": "2025-09-02", "razon": "Mantenimiento preventivo"}
    }
}