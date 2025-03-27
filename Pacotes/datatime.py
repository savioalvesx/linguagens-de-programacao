import datetime

agora = datetime.datetime.now()

print("Data e hora atual: ", agora)
print("Dia Atual: ", agora.day)
print("Mês Atual: ", agora.month)
print("Ano Atual: ", agora.year)
print("Horas Atual: ", agora.hour)
print("Minutos Atual: ", agora.minute)
print("Segundos atual: ", agora.second)


if agora.hour > 18:
    print("Boa Noite!")
elif agora.hour >= 18 and agora.hour < 18:
    print("Boa Tarde!")
else: 
    print("Bom dia!")