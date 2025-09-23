import math
import random


def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)


def evalua_ruta(ruta, coord):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total


def i_hill_climbing(coord):
    # Crear ruta inicial aleatoria
    ruta = list(coord.keys())  # Inicializa la ruta con todas las ciudades
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        mejora = False
        # Genera nueva ruta aleatoria
        random.shuffle(ruta)
        for i in range(len(ruta)):
            for j in range(i + 1, len(ruta)):
                ruta_tmp = ruta[:]
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                dist = evalua_ruta(ruta_tmp, coord)
                if dist < evalua_ruta(ruta, coord):
                    # Se encuentra un vecino que mejora el resultado
                    mejora = True
                    ruta = ruta_tmp[:]
        max_iteraciones -= 1

        if evalua_ruta(ruta, coord) < evalua_ruta(mejor_ruta, coord):
            mejor_ruta = ruta[:]

    return mejor_ruta


if __name__ == "__main__":
    coord = {
        'JiloYork': (19.984146, -99.519127),
        'Toluca': (19.286167856525594, -99.65473296644892),
        'Atlacomulco': (19.796802401380955, -99.87643301629244),
        'Guadalajara': (20.655773344775373, -103.35773871581326),
        'Monterrey': (25.675859554333684, -100.31405053526082),
        'Cancún': (21.158135651777727, -86.85092947858692),
        'Morelia': (19.720961251258654, -101.15929186858635),
        'Aguascalientes': (21.88473831747085, -102.29198705069501),
        'Queretaro': (20.57005870003398, -100.45222862892079),
        'CDMX': (19.429550164848152, -99.13000959477478)
    }

    mejor_ruta = i_hill_climbing(coord)
    print(mejor_ruta)
    print("Distancia total:", evalua_ruta(mejor_ruta, coord))