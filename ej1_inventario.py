# ej1_inventario.py  
inventario = { 
    "espada_corta": {"categoria": "arma", "peso": 1}, 
    "capa_elfica": {"categoria": "objeto_magico", "peso": 0}, 
    "pan_de_camino": {"categoria": "provision", "peso": 1}, 
    "daga": {"categoria": "arma", "peso": 1}, 
    "frasco_de_galadriel": {"categoria": "objeto_magico", "peso": 0}, 
}  

def clasificar_inventario(inventario):
    armas = []
    provisiones = []
    objetos_magicos = []

    for nombre_item, datos in inventario.items():
        categoria = datos.get("categoria")
        if categoria == "arma":
            armas.append(nombre_item)
        elif categoria == "provision":
            provisiones.append(nombre_item)
        elif categoria == "objeto_magico":
            objetos_magicos.append(nombre_item)

    return armas, provisiones, objetos_magicos

if __name__ == "__main__":
    armas, provisiones, objetos_magicos = clasificar_inventario(inventario)
    print("Armas", armas)
    print("Provisiones", provisiones)
    print("Objetos mágicos", objetos_magicos)