import utils as ut

tablero_user = ut.crear_tablero()
#tablero_cpu = crear_tablero()
#barco_1=[(0,1),(1,1)]
#barco_2=[(3,4),(3,5),(3,6),(3,7)]

#print(tablero_user)
#print(tablero_cpu)
#colocar_barco(barco_1,tablero_user)
#colocar_barco(barco_2,tablero_user)
#disparar((0,1),tablero_user)
#crear_barco(4)
barcos = ut.generar_barcos(tablero_user)
print(barcos)
#print(ut.colocar_barcos(barcos,tablero_user))