import datetime

# Registro diário de rotina
data = datetime.date.today()
hora_dormiu = input("Que horas você dormiu? ")
hora_acordou = input("Que horas você acordou? ")
tempo_tela_min = int(input("Qual foi o seu tempo de tela (em minutos)? "))
estudo_min = int(input("Por quanto tempo você estudou (em minutos)? "))
hobbies_min = int(input("Quanto tempo dedicou aos seus hobbies (em minutos)? "))
nivel_energia = int(input("Qual foi o seu nível de energia hoje? "))

print(f"\nData de hoje: {data}")
print(f"Hora que dormiu: {hora_dormiu}")
print(f"Hora que acordou: {hora_acordou}")
print(f"Tempo de tela: {tempo_tela_min}")
print(f"Tempo para estudos: {estudo_min}")
print(f"Tempo para hobbies: {hobbies_min}")
print(f"Nível de energia: {nivel_energia}")