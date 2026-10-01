# ej6_anillounico.py
# parametros asignados
PODER_INICIAL = 40
MI_LEGAJO = "123456"

# resultado obtenido del ejercicio 4
CAMINOS_BOSQUE = 89

class AnilloUnico:
    """TAD que reemplaza el Anillo Único, encapsulando su poder interno."""

    def __init__(self, poder_inicial=0):
        #atributo encapsulado
        self._poder = 0
        self.forjar(poder_inicial)

    def forjar(self, poder_inicial):
        """Establece el poder inicial garantizando que esté en rango."""
        if 0<= poder_inicial <=100:
            self._poder = poder_inicial
        else:
            self._poder = 100
            print("Aviso: el poder de forja superaba el limite y se fijó en 100.")

    def usar(self, intensidad):
        """Aumenta el poder del anillo sin permitir que que supere 100."""
        if self._poder + intensidad > 100:
            print(
                "¡Aviso! El anillo se corrompe: el poder intentó superar el máximo permitido de 100."
            )
            self._poder = 100
        else:
            self._poder += intensidad
    
    def consultar_poder(self):
        """Único método permitido para leer el poder actual desde afuera."""
        return self._poder

# prueba y sello final
if __name__ == "__main__":
    mi_anillo = AnilloUnico(PODER_INICIAL)
    print("Poder inicial del anillo:", mi_anillo.consultar_poder())

    # usar el anillo al menos una vez
    mi_anillo.usar(25)
    print("Poder del anillo tras usarlo:", mi_anillo.consultar_poder())

    # al final de ej6_anillounico.py  
    LEGAJO = MI_LEGAJO  
    CAMINOS_BOSQUE = 89  
    sello_final = f"COD-{LEGAJO}-{(CAMINOS_BOSQUE * 7 + sum(ord(c) for c in LEGAJO)) % 10000}"  
    print("Sello Final:", sello_final)
