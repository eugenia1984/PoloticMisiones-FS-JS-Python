"""
4. Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales

# Busque esta información
# time() : returns the time as a floating point number expressed in seconds since the epoch, in UTC
# timedelta() : es la diferencia de tiempo, puede ser años (years= ), meses(months= ), semanas (weeks= ), dias (days= ), horas (hours= ), minutos (minutes= ), segundos (seconds= ) 
"""
#Importa datetime
import datetime

# Declaro variable mi_hora y asigno el valor de la hora actual
mi_hora = datetime.datetime.now()
# Declaro una variable hora_auxiliar de dos horas
hora_auxiliar = datetime.timedelta(hours=2)
# Le sumo dos horas con mi variable hora_auxiliar a mi hora actual
hora_mas_dos = (mi_hora + hora_auxiliar).time()

#Muestro por consola
print(f'La hora actual es: {mi_hora.time()} y si le sumo dos hora son las {hora_mas_dos}')

