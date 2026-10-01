# ej4_bosqueviejo.py   

PASOS_ASIGNADOS = 10

def formas_de_subir(escalones):  
    # Caso base y caso recursivo. Sin loops, sin cache.   
    if escalones <= 0:
        return 0
    if escalones == 1:
        return 1
    if escalones == 2:
        return 2
    # caso recursivo(suma de las dos opciones de llegada)
    return formas_de_subir(escalones - 1) + formas_de_subir(escalones - 2) 

# ejecuto y guardo la variable 
CAMINOS_BOSQUE = formas_de_subir(PASOS_ASIGNADOS)
print("Caminos posibles:", CAMINOS_BOSQUE)
