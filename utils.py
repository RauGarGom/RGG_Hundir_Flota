import numpy as np
import random as rd

###Variables generales
Acierto = False ### Para la recursividad del turno. Se vuelve True si def disparar acierta

def crear_tablero(largo = 10):
    tablero = np.full ((largo,largo), "_")
    return(tablero)

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
        Acierto = True
        print("¿Acierto?",Acierto)
    else:
        print("Agua")
        tablero[casilla] = "A"
        Acierto = False
        print("¿Acierto?",Acierto)
    return tablero

def crear_barco(eslora):
    casilla_0 = (rd.randint(0,9), rd.randint(0,9))
    orientacion = rd.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal
    return barco

### Generador de barcos
def generar_barcos(tablero):
    longs = [2,2,2,3,3,4]
    barcos = []
    celdas_usadas = []

    ### Comparamos si la lista de barcos tiene los mismos elementos que los barcos a crear.
    ### Se intenta crear un barco con la eslora indicada. Si sus coordenadas no están en el listado de celdas usadas, lo crea. 
    while len(barcos) < len(longs):
        barcos = []
        celdas_usadas = []
        ### Creamos un intento de barco
        for i,x in enumerate(longs):
            sum_barco = 0
            intento_barco = crear_barco(x)
            ### Revisamos el intento de barco. Si cuenta con todas las posiciones correctas, se lo lleva al listado de barcos.
            for pos in range(len(intento_barco)):
                if intento_barco[pos] not in celdas_usadas:
                    sum_barco += 1
                else:
                    i -= 1
                    x -= 1
                    break
            ### Con esto me quedo con las celdas usadas
            if sum_barco == len(intento_barco):
                barcos.append(intento_barco)
                for j,y in enumerate(barcos):
                    for k,z in enumerate(barcos[j]):
                        celdas_usadas.append(barcos[j][k])      
    return barcos

###TODO: Borrar??
# def colocar_barcos(barcos,tablero):
#     ### Ya tenemos los barcos creados. Los colocamos
#     for indice,casilla in enumerate(barcos):
#         for casilla in barcos[indice]:
#             try:
#                 tablero[casilla] = "O"
#             except:
#                 colocar_barcos(barcos,tablero)
#     return(tablero)

##TODO: Por alguna razón, he tenido que meter el casilla -1. Eso hace que haya barcos que no se generen. Cuidado con el loop del diablo
def colocar_barcos(barcos,tablero):
    ### Ya tenemos los barcos creados. Los colocamos. Revisamos la fila y la columna de cada uno, y si no se encuentra, ponemos una "O"
        for posicion in barcos:
            for fila, columna in posicion:
                casilla=(fila-1,columna-1) ###Revisar por qué tengo que restarle 1 para que no pete
                try:
                    if tablero[casilla] == "O":
                        generar_barcos(tablero)
                    else:
                        try:
                            tablero[casilla] = "O"
                        except:
                            colocar_barcos(barcos,tablero)
                except:
                    print(f"Error en la colocación de barcos en el tablero {tablero}. Vuelve a ejecutar")
                    # colocar_barcos(barcos,tablero)
        return tablero


###TODO Sistema de turnos. Falta recursividad en turnos (acierto = sigue turno), quitar disparos ya utilizados por CPU
###TODO Ocultar tablero de rival
###TODO Finalizar la partida (count(O) == 0 en algún tablero)
###TODO Meter tiempo para que sea algo mejor
def turnos(tablero_us,tablero_rv):
    jugador = 0
    turnos = 1
    while turnos <= 10: ###TODO: Quitar cuando tengamos final
        print("Turno:", turnos)
        if jugador == 0:
            print("Turno del jugador")
            print("Tablero del rival:")
            print(tablero_rv)
            us_fila = int(input("Introduce la fila: "))
            us_columna = int(input("Introduce la columna: "))
            us_coord = (us_fila-1,us_columna-1) ### Nadie se refiere a la primera fila y columna como 0,0
            tablero_rv = disparar(us_coord,tablero_rv)
            if Acierto == False: ### Se vuelve True cuando se acierta, y False cuando se falla
                jugador = 1
                turnos += 1
        else:
            print("Turno del ordenador")
            rv_fila = rd.randint(0,9)
            rv_columna = rd.randint(0,9)
            rv_coord = (rv_fila,rv_columna)
            print("El ordenador dispara a",rv_coord)
            tablero_us = disparar(rv_coord,tablero_us)
            print(tablero_us)
            if Acierto == False:
                jugador = 0
                turnos += 1
    else:
        print("Final del juego!")