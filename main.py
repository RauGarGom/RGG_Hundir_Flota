import utils as ut

#Acierto = False

### Pruebas crear tablero
tablero_user = ut.crear_tablero()
tablero_rival = ut.crear_tablero()

### Pruebas generar barcos
barcos_user = ut.generar_barcos(tablero_user)
barcos_rival = ut.generar_barcos(tablero_rival)
# print(tablero_user)
# print(barcos_user)


### Pruebas colocar barcos
tablero_user = ut.colocar_barcos(barcos_user,tablero_user)
tablero_rival = ut.colocar_barcos(barcos_rival,tablero_rival)

### Pruebas turnos
ut.turnos(tablero_user,tablero_rival)