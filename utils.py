import numpy as np
import random as rd

###Variables generales
acierto = False ### Para la recursividad del turno. Se vuelve True si def disparar acierta


def crear_tablero(largo = 10):
    tablero = np.full ((largo,largo), "_")
    return(tablero)

def disparar(casilla,tablero,tablero_oc,jugador):
    tr_jugador = jugador
    if tablero[casilla] == "O":
        print("Tocado")
        acierto = True
        rep_tiro = False
        tablero[casilla] = "X"
        if tr_jugador == 0:
            tablero_oc[casilla] = "X"
    elif tablero[casilla] == "X" or tablero[casilla] == "A": ###TODO: Seguro que se puede poner más bonito
        print("¡Ya has disparado ahí! Vuelve a probar")
        rep_tiro = True
        acierto = False
    else:
        print("Agua")
        tablero[casilla] = "A"
        if tr_jugador == 0:
            tablero_oc[casilla] = "A"
        acierto = False
        rep_tiro = False
    return [tablero, acierto, rep_tiro, tablero_oc] ### Lista para poder seleccionar qué valor quiero cuando la llame

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




###TODO Meter tiempo para que sea algo mejor
###TODO Seguro que se puede comprimir el código de la lógica de turnos. Mucho código repetido
def turnos(tablero_us,tablero_rv,tablero_rv_oc,jugador,turnos,trampas):
    trampa = trampas
    us_punt = 0
    rv_punt = 0
    while us_punt < 5 and rv_punt < 5:
        print("--------------")
        print("Turno:", turnos)
        if jugador == 0: ## Es decir, si es turno del usuario
            print("Turno del jugador")
            if trampa == True:
                print("Tablero del rival:")
                print(tablero_rv)
            else:
                print("Tablero oculto del rival:")
                print(tablero_rv_oc)
            us_fila = int(input("Introduce la fila: "))
            us_columna = int(input("Introduce la columna: "))
            us_coord = (us_fila-1,us_columna-1) ### Nadie se refiere a la primera fila y columna como 0,0
            resultado_us = disparar(us_coord,tablero_rv,tablero_rv_oc,jugador) ### Me guardo todos los resultados de la lista de disparar
            tablero_rv = resultado_us[0]
            acierto = resultado_us[1]
            rep_tiro = resultado_us[2]
            if acierto == True: ### Se vuelve True cuando se acierta, y False cuando se falla
                jugador = 0
                turnos = turnos
                us_punt += 1
                print("Tu puntuación:", us_punt)
            elif rep_tiro == True: ### Se vuelve True cuando se apunta a una X o una A
                jugador = 0
                turnos = turnos
            else:
                jugador = 1
                turnos += 1
        else:
            print("Turno del ordenador")
            rv_fila = rd.randint(0,9)
            rv_columna = rd.randint(0,9)
            rv_coord = (rv_fila,rv_columna)
            print("El ordenador dispara a",rv_coord)
            resultado_rv = disparar(rv_coord,tablero_us,tablero_rv_oc,jugador)
            tablero_us = resultado_rv[0]
            acierto = resultado_rv[1]
            rep_tiro = resultado_us[2]
            print(tablero_us)
            if acierto == True or rep_tiro == True:
                jugador = 1
                turnos = turnos
                rv_punt += 1
                print("Puntuación del ordenador:",rv_punt)
            elif rep_tiro == True:
                jugador = 1
                turnos = turnos
            else:
                jugador = 0
                turnos += 1
    else:
        print("="*50)
        if us_punt > rv_punt:
            print("¡¡ENHORABUENA!! Has ganado")
        else:
            print("¡Has perdido! Suerte la próxima vez")
        print("="*50)
        print("¡Final del juego! Dame más tiempo para mejorarlo si te ha gustado :D")
        print("="*50)