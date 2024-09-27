import utils as ut
### Variables generales
acierto = False ### Para la recursividad del turno. Se vuelve True si def disparar acierta
jugador = 0
turnos = 1

##INICIO
### ¿Queremos hacer trampas?
trampas_in = (str(input('¡Hola! ¿Te gustaría hacer trampas? (Responde "SI" o "NO"): ')))
if trampas_in == "SI":
    trampas_jg = True
else:
    trampas_jg = False

### Creamos 3 tableros
tablero_user = ut.crear_tablero()
tablero_rival = ut.crear_tablero()
tablero_rival_oc = ut.crear_tablero()

### Generamos 2 listas de barcos
barcos_user = ut.generar_barcos(tablero_user)
barcos_rival = ut.generar_barcos(tablero_rival)

### Colocamos los barcos en sus respectivos tableros
tablero_user = ut.colocar_barcos(barcos_user,tablero_user)
tablero_rival = ut.colocar_barcos(barcos_rival,tablero_rival)

### Pruebas turnos
ut.turnos(tablero_user,tablero_rival,tablero_rival_oc,jugador,turnos,trampas_jg)