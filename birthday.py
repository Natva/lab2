# Proyecto: Cumpleaños 
# Autor: Natalia Vàsquez 
# Carnet: 1596620
# este programa encuentre la edad de una persona a base de su fecha, mes y anos
from datetime import date

# La fecha de actual
hoy= date.today()

# el mes actual 
hoy = hoy.months()

# el ano 'actual' 
hoy = hoy.years()

# obtener los datos de la persona 
print ('bienvenido al programa que calculara tu edad')

# obtener la fecha de nacimiento de la persona 
diade_naci = input('¿cual es la fechad e tu nacimiento?')
diade_naci = input(diade_naci)

# obtener el mes de nacimineto de la persona 
mesde_naci = input('¿cual es el mes en que naciste')
mesde_naci = input(mesde_naci) 

# obtener el año en que nacio la persona 
year_de_naci = input('¿cual es el ano en que naciste')
year_de_naci = input('yearde_naci')

diff_year = hoy.years - year_de_naci 
diff_mes = hoy.months - mesde_naci
diff_dia = hoy.date.day - diade_naci
diff_year-='(( mes :  dia) < (mesde_naci . diade_naci))
# String - cadena - str
print('Tus_anos_son' + str(diff_year + 'anos' + str(diff_mes) + 'meses' + str(diff_dia) + 'dias'))