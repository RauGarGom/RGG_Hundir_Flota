import numpy as np
import random as rd

def crear_tablero(largo = 10):
    tablero = np.full ((largo,largo), "_")
    return(tablero)

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
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


def generar_barcos(tablero):
    longs = [2,2,2,3,3,4]
    barcos = []
    celdas_usadas = []
    #check= set() ### Set donde guardar las tuplas
    '''
    Comparamos si la lista de barcos tiene los mismos elementos que los barcos a crear.
    Se intenta crear un barco con la eslora indicada. Si sus coordenadas no están en el listado de celdas usadas, lo crea. 
    '''
    while len(barcos) < len(longs):
        barcos = []
        celdas_usadas = []
        ### Creamos un intento de barco
        for i,x in enumerate(longs):
            sum_barco = 0
            print("Creando barco",i+1)
            intento_barco = crear_barco(x)
            print(intento_barco)
            ### Revisamos el intento de barco. Si cuenta con todas las posiciones correctas, se lo lleva al listado de barcos.
            for pos in range(len(intento_barco)):
                if intento_barco[pos] not in celdas_usadas:
                    sum_barco += 1
                else:
                    print("Barco no creado")
                    i -= 1
                    x -= 1
                    #colocar_barcos(tablero)
                    break
            ### Con esto me quedo con las celdas usadas
            if sum_barco == len(intento_barco):
                barcos.append(intento_barco)
                for j,y in enumerate(barcos):
                    for k,z in enumerate(barcos[j]):
                        celdas_usadas.append(barcos[j][k])
                # print("-------------")
                # print("Barco creado:", intento_barco)
                # print("Sum barcos:",sum_barco,"Len barcos:",len(intento_barco))
                # print("Listado de barcos:", barcos)
                # print("Celdas usadas:",celdas_usadas)
        ### Ya tenemos los barcos creados. Los colocamos
        # for indice,casilla in enumerate(barcos):
        #     for casilla in barcos[indice]:
        #         try:
        #             tablero[casilla] = "O"
        #         except:
        #             colocar_barcos(tablero)
            # print(tablero)          
    return barcos

def colocar_barcos(barcos,tablero):
    ### Ya tenemos los barcos creados. Los colocamos
    for indice,casilla in enumerate(barcos):
        for casilla in barcos[indice]:
            try:
                tablero[casilla] = "O"
            except:
                colocar_barcos(barcos,tablero)
    return(tablero)