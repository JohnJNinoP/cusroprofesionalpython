import datetime
import pytz


my_time = datetime.datetime.now()
print(my_time)

my_day = datetime.date.today()
print(my_day)
print(my_day.year)
print(my_day.month)
print(my_day.day)

my_datetime = datetime.datetime.now()
print(my_datetime)
my_str = my_datetime.strftime('%d/%m/%Y')
print("Format LATAM " + my_str)

my_str = my_datetime.strftime('%m/%d/%Y')
print("Format USA " + my_str)

my_str = my_datetime.strftime('Estamos en el año %Y')
print("Format Ramdom " + my_str)


bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.datetime.now(bogota_timezone)
print(bogota_date.strftime("%d/%m/%Y, %H:%M:%S" ))


mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.datetime.now(mexico_timezone)
print(mexico_date.strftime("%d/%m/%Y, %H:%M:%S" ))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.datetime.now(caracas_timezone)
print(caracas_date.strftime("%d/%m/%Y, %H:%M:%S" ))