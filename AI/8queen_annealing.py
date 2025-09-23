import math
import random
import matplotlib.pyplot as plt

# -------------------------
# Distance Function
# -------------------------
def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# -------------------------
# Evaluate Route
# -------------------------
def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    # return to start
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

# -------------------------
# Hill Climbing Algorithm
# -------------------------
def i_hill_climbing(coord):
    ruta = list(coord.keys())       # initial route
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        mejora = False
        random.shuffle(ruta)        # random start
        for i in range(len(ruta)):
            for j in range(i + 1, len(ruta)):
                ruta_tmp = ruta[:]
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                if evalua_ruta(ruta_tmp, coord) < evalua_ruta(ruta, coord):
                    ruta = ruta_tmp[:]
                    mejora = True

        max_iteraciones -= 1

        if evalua_ruta(ruta, coord) < evalua_ruta(mejor_ruta, coord):
            mejor_ruta = ruta[:]

    return mejor_ruta

# -------------------------
# Plotting Function
# -------------------------
def plot_route(ruta, coord):
    plt.figure(figsize=(8, 6))

    # Extract coordinates in order
    x = [coord[city][1] for city in ruta] + [coord[ruta[0]][1]]
    y = [coord[city][0] for city in ruta] + [coord[ruta[0]][0]]

    # Draw route
    plt.plot(x, y, '-o', color="blue", linewidth=2, markersize=8)

    # Annotate city names
    for city in ruta:
        plt.text(coord[city][1] + 0.1, coord[city][0] + 0.1, city, fontsize=9)

    plt.title("Best Route Found by Hill Climbing")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()

# -------------------------
# Main
# -------------------------
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
    print("Best route:", mejor_ruta)
    print("Total distance:", evalua_ruta(mejor_ruta, coord))

    # Plot the result
    plot_route(mejor_ruta, coord)
