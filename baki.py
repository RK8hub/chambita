import pickle
# Guardar lista de objetos
def guardar_objetos(ruta,lista_objetos):
    with open(f"{ruta}.pkl", "wb") as f:
        pickle.dump(lista_objetos, f)

def cargar_objetos(ruta):
    with open(f"{ruta}.pkl", "rb") as f:
        lista_objetos = pickle.load(f)
        return lista_objetos
