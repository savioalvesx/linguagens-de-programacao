import datetime

print("Este programa que exibe uma saudação de acordo com o horário atual.\n")

horas = datetime.datetime.now()

print(f"Horas Atual: {horas.hour}:{horas.minute}:{horas.second} ") 

if horas.hour >= 0 and horas.hour < 12:
    print("Bom dia!")
elif horas.hour >= 12 and horas.hour < 18:
    print("Boa Tarde!")
else: 
    print("Boa noite!")

# Manhã: das 00h00 (meia-noite) até 11h59.
# Tarde: das 12h00 (meio-dia) até 17h59.
# Noite: das 18h00 até 23h59.