# Ejercicio 03
# Desarrolla una función o procedimiento que estime el tiempo de entrega de la entrega de una compra online (en días),
# en función de la distancia que existe entre una dirección de origen y destino.
# Suponga que los envíos siempre se despachan desde el mismo origen.
# Para la determinación de la distancia entre el origen y destino genere números aleatorios entre 0 km y 2.000 km
# Asuma que el tiempo de despacho está determinado por una sucesión numérica,
# donde cada N término se relaciona con un incremento en un rango de distancia entre la dirección de origen y de destino
# como se muesta a continuación:
# Rango 1. Menos de 100 km, se entregan el mismo día (Día cero)
# Rango 2. Menos de 200 km, se entregan al día siguiente (Día uno)
# Rango 3. Menos de 300 km, se entregan al día siguiente (Día uno)
# Rango 4. Menos de 400 km, se entregan al día subsiguiente (Día dos)
# Rango 5. Menos de 500 km, se entregan al tercer día (Día tres) ...
# Rango n. Menos de n km, Los días de entrega se calculan como la suma de los días de entrega de los rangos n–1 y n-2
import random

def get_tiempo_de_entrega(distancia):
    rango = 0
    rangos_distancia = []
    item = {}
    for i in range(int(distancia/100)+1):
        rango +=100
        if i <= 1:
            dias = i
        else:
            rango_n1 = rangos_distancia[i-1] #n–1
            rango_n2 = rangos_distancia[i-2] #n-2
            dias = rango_n1["dias"] + rango_n2["dias"]
        item = {"orden":(i+1),"rango":rango,"dias": dias}
        rangos_distancia.append(item)
    return item

distancia = random.randrange(2000)
print("Distancia aleatoria entre origen y destino: ",distancia,"km")
rango_distancia = get_tiempo_de_entrega(distancia)
print("Total dias de entrega : ",rango_distancia['dias'])
print("Rango ",rango_distancia["orden"],": menos de {} km".format(rango_distancia["rango"]),",se entrega en {} dias".format(rango_distancia["dias"]))
