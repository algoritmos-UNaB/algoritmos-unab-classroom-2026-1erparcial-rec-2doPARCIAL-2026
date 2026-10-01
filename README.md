## Algoritmos y Estructuras de Datos
### 1er PARCIAL RECUPERATORIO - MARTES - 30/06/26 - Comisión 2 -

--------------------------------------------------------------------------------

##### 📌 **Modalidad**
* 🗓️ **Fecha:** Martes **30/06**
* 🕖 **Disponibilidad:** desde las **18:00 hs.** hasta las **01:45 hs.**.
* ⏱️ **Duración máxima:** **3 (tres) horas ** desde el momento en que aceptan la actividad en **GitHub ClassRoom**.
* 🧪 **Intentos:** Solo **1 (uno)**.
* 📢 **Publicación de notas:** a más tardar el **Jueves**.
⚠️ **IMPORTANTE:** deben estar conectados al Meet, **SE CONSIDERAN AUSENTES AQUELLOS/AS ALUMNOS/AS QUE NO SE CONECTEN**.

⚠️ **IMPORTANTE:** Al final del archivo README.md, **DEBEN completar sus datos personales** (nombre completo, número de legajo y correo institucional).

--------------------------------------------------------------------------------
## Parcial I — La Comunidad del Código
**Libro Primero · De la Comarca a Rivendel**

### Prólogo del Escriba
Antes de que la Comunidad pueda partir de Bolsón Cerrado, el Concilio de Elrond exige una prueba: quien quiera acompañar al portador del Anillo hasta Rivendel debe demostrar que comprende el lenguaje con el que los Magos cifran sus mapas, sus cuentas y sus hechizos. Ese lenguaje es Python. Este pergamino contiene seis pruebas. Cada una está sellada con tu propio legajo: nadie más en Mediatierra recibirá exactamente los mismos números que vos.

### Identificación y Sello del Pergamino
* **Distancia Comarca→Bree:** [120] km — usar en Ejercicio II
* **Millas iniciales recorridas:** [completar] — usar en Ejercicio II
* **Pasos del Bosque Viejo:** [completar] — usar en Ejercicio IV
* **Poder inicial del Anillo:** [completar] — usar en Ejercicio VI

### Instrucciones Generales
1. Este parcial está **personalizado por Uds.**. Completá el campo de arriba antes de empezar: todos los parámetros marcados en rojo dependen de tus números.
2. No se permiten librerías externas salvo que el ejercicio lo indique explícitamente. Lo pedido se resuelve con Python estándar.
3. Cada ejercicio de código va en un archivo `.py` separado, nombrado exactamente como se indica en cada consigna.
4. Las respuestas teóricas (Ejercicios I, III y V) se entregan en un único archivo `teoria.txt`, identificando claramente cada respuesta.
5. El Ejercicio VI exige imprimir un **Sello Final** por consola. Ese sello se valida cruzando tu legajo con tu propio resultado del Ejercicio IV: si copiaste o adivinaste, no va a coincidir.

---

### I. El inventario de Bolsón Cerrado (15 pts)
**Unidad 1 · Tipos de datos**
Bilbo, antes de desaparecer en su fiesta de cumpleaños, deja a Frodo un inventario desordenado de todo lo que hay en el agujero-hobbit.

**a) Teórica (6 pts).** Bilbo guardó el *mapa de la Comarca* en una tupla de coordenadas y el *saco de provisiones* en una lista. Explicá, en no más de 8 líneas, por qué esa elección tiene sentido en términos de mutabilidad, y qué problema aparecería si se intercambiaran los tipos.

**b) Código (9 pts), archivo `ej1_inventario.py`.** Se te da el siguiente diccionario. Escribí una función `clasificar_inventario(inventario)` que devuelva tres listas: `armas`, `provisiones` y `objetos_magicos`, separando los ítems según la clave `"categoria"`.
```python
# ej1_inventario.py  
inventario = { 
    "espada_corta": {"categoria": "arma", "peso": 1}, 
    "capa_elfica": {"categoria": "objeto_magico", "peso": 0}, 
    "pan_de_camino": {"categoria": "provision", "peso": 1}, 
    "daga": {"categoria": "arma", "peso": 1}, 
    "frasco_de_galadriel": {"categoria": "objeto_magico", "peso": 0}, 
}  

def clasificar_inventario(inventario):  
    # Completar: devolver (armas, provisiones, objetos_magicos)   
    pass
```
### II. El sendero hacia Bree (15 pts)
**Unidad 2 · Funciones La Comunidad abandona la Comarca.**
 La Comunidad abandona la Comarca. Cada legua que avanzan se suma a un contador colectivo que todos comparten, aunque marchen en grupos separados.
  
  Código, archivo `ej2_sendero.py`. La distancia entre la Comarca y Bree para tu legajo es de [completar] km, y la Comunidad ya recorrió [completar] millas. Implementá:
 - Una variable global `millas_recorridas` inicializada con tus millas iniciales.
 - Una función `avanzar(km, velocidad=5)` que reciba kilómetros a recorrer y una velocidad por defecto (leguas/hora), calcule las horas necesarias, y modifique la variable global `millas_recorridas` sumando el equivalente recorrido (usá 1 km ≈ 0.62 millas).
 - Una función `resumen_viaje()` que imprima cuántas horas tardaría la Comunidad en llegar a Bree con la velocidad por defecto, y el valor actualizado de `millas_recorridas` después de llamarla.

### III. El Consejo habla en voz baja (10 pts)
**Unidad 2 · Alcance Teórica.** 
En la posada de Bree, Pippin intenta "ayudar" modificando una variable dentro de una función sin avisarle a nadie. El resultado no es el esperado.

Teórica. Mostrá un pequeño fragmento de código (de no más de 6 líneas) donde una función intenta modificar una variable global sin declararla `global`, y explicá: (1) qué ocurre realmente con esa variable dentro de la función, (2) qué valor queda afuera después de llamar a la función, y (3) cómo lo arreglarías.

### IV. El Bosque Viejo (20 pts)
**Unidad 3 · Recursividad**
 El Viejo Hombre Sauce enreda los senderos del bosque. Para salir, los hobbits deben subir una escalinata embrujada de [completar] escalones, avanzando de a 1 o 2 escalones por vez. El bosque solo deja pasar a quien calcula de cuántas formas distintas se puede subir esa escalinata.
 
 Código, archivo `ej4_bosqueviejo.py`. Implementá `formas_de_subir(escalones)` que devuelva la cantidad de formas distintas de subir la escalinata. Requisito obligatorio: la función debe ser puramente recursiva, sin memoización, sin estructuras auxiliares y sin bucles. Llamala con tu cantidad de escalones, mostrá el resultado por consola y guardá ese resultado en la variable `CAMINOS_BOSQUE`. lo vas a necesitar en el Ejercicio VI.
```python
# ej4_bosqueviejo.py   
def formas_de_subir(escalones):  
    # Caso base y caso recursivo. Sin loops, sin cache.   
    pass  

CAMINOS_BOSQUE = formas_de_subir( PASOS_ASIGNADOS )  # reemplazar PASOS_ASIGNADOS por tu valor  
print("Caminos posibles:", CAMINOS_BOSQUE)
```
### V. La maldición del Bosque Viejo (10 pts)
**Unidad 3 · Caso base Teórica.**
Merry jura que si alguien olvida el caso base al subir la escalinata embrujada, el bosque lo atrapa para siempre.

Teórica. Tomando como referencia tu función `formas_de_subir` del Ejercicio IV: identificá explícitamente cuál es el caso base, cuál el caso recursivo, y explicá qué ocurriría en la ejecución real (no en abstracto) si el caso base se eliminara por completo. ¿Qué error de Python esperarías ver?

### VI. El Anillo Único (30 pts)
**Unidad 4 · TAD / Encapsulamiento**
En Rivendel, Elrond explica que el `Anillo Único` es, ante todo, un Tipo Abstracto de Datos: nadie debería poder tocar su poder interno directamente, solo a través de las operaciones que el propio Anillo decide exponer. Tu poder inicial asignado es [completar].

 Código, archivo `ej6_anillounico.py`. Implementá una clase AnilloUnico que actúe como un verdadero TAD:
 - Un atributo de poder encapsulado (no accesible directamente desde afuera de la clase, ej. _poder o con doble guion bajo).
 - Un método `forjar(poder_inicial)` (o vía constructor) que establezca el poder inicial sin exponerlo directamente. Tu poder inicial asignado es [completar].
 - Un método usar(intensidad) que aumente el poder interno en esa intensidad, pero que nunca permita superar 100 (si se supera, el Anillo "corrompe" y debe lanzar una excepción o imprimir un aviso sin romper el encapsulamiento).
 - Un método `consultar_poder()` que sea la única forma permitida de leer el poder actual desde afuera.

Al final del archivo, instanciá el Anillo con tu poder inicial, usalo al menos una vez, y luego imprimí el Sello Final con esta línea exacta:
```python
# al final de ej6_anillounico.py  
LEGAJO = "TU_LEGAJO_AQUI"  
CAMINOS_BOSQUE = PEGAR_AQUI_EL_RESULTADO_DEL_EJERCICIO_IV  
sello_final = f"COD-{LEGAJO}-{(CAMINOS_BOSQUE * 7 + sum(ord(c) for c in LEGAJO)) % 10000}"  
print("Sello Final:", sello_final)
```
--------------------------------------------------------------------------------

##### Por Favor Completar sus Datos

<u> **Nombre y Apellido:** Matias Sanguinetti </u>

<u> **Email:** </u>

<u> **Comisión:** </u>

--------------------------------------------------------------------------------
