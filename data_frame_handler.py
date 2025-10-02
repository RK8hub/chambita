import pandas as pd
import inspect
import os

def exportar(data, ruta):
    db = pd.json_normalize(data) if not isinstance(data, pd.DataFrame) else data
    
    # sacar extensión
    base, ext = os.path.splitext(ruta)
    if not ext:
        raise ValueError("Debes poner la extensión (ej: datos.csv, datos.xlsx)")
    formato = ext.lstrip(".").lower()

    # armar dict de métodos disponibles
    metodos = {m[3:]: m for m, f in inspect.getmembers(pd.DataFrame, inspect.isfunction) if m.startswith("to_")}
    
    if formato not in metodos:
        raise ValueError(f"Formato '{formato}' no soportado. Soportados: {list(metodos.keys())}")
    
    # llamar dinámicamente
    metodo = getattr(db, metodos[formato])
    
    # algunos métodos requieren index=False para no ser molestos
    kwargs = {"index": False} if "index" in inspect.signature(metodo).parameters else {}
    metodo(ruta, **kwargs)
    
    return ruta
