# ej2_sendero.py
DISTANCIA_KM = 120 #km asignados
MILLAS_INICIALES = 50 # millas asignadas

# var global inicializada
millas_recorridas = MILLAS_INICIALES

def avanzar(km, velocidad=5):
    """Calcula las horas necesarias para recorrer los km a una velocidad dada
    (en leguas/hora) y actualiza la variable global millas_recorridas.
    """
    global millas_recorridas

    # 1 legua=5km -> leguas a recorrer=km/5
    leguas = km / 5
    horas = leguas / velocidad

    # conversion a millas 1 km ≈ 0.62 millas
    millas_nuevas = km * 0.62
    millas_recorridas += millas_nuevas

    return horas

def resumen_viaje():
    # calcula las horas con la veloc por defecto (5 leguas/h)
    horas_totales = avanzar(DISTANCIA_KM, velocidad=5)

    print(
        f"Horas necesarias para llegar a Bree: {horas_totales:.2f} horas."
    )
    print(
        f"Millas totales recorridas (actualizado): {millas_recorridas:.2f} millas."
    )

if __name__ == "__main__":
    resumen_viaje()