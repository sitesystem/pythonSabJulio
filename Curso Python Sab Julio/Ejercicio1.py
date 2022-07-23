import datetime

día = datetime.date.today().day
mes = datetime.date.today().month
año = datetime.date.today().year

print(día)
print(mes)
print(año)

print(datetime.date.today())    # Fecha Actual
print(datetime.datetime.now())  # Fecha y Hora Actual