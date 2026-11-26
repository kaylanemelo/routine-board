import datetime
import csv
import os

# Pede um horário até vir no formato HH:MM e devolve sempre uma string padronizada
def pedir_hora(pergunta):
    while True:
        resposta = input(pergunta)
        try:
            horario = datetime.datetime.strptime(resposta, "%H:%M")

            return horario.strftime("%H:%M")
        except ValueError:
            print("Formato inválido! Digite no padrão HH:MM (ex: 22:30).")


# Registro diário de rotina
data = datetime.date.today()
hora_dormiu = pedir_hora("Que horas você dormiu (HH:MM)? ")
hora_acordou = pedir_hora("Que horas você acordou (HH:MM)? ")
tempo_tela_min = int(input("Qual foi o seu tempo de tela (em minutos)? "))
estudo_min = int(input("Por quanto tempo você estudou (em minutos)? "))
hobbies_min = int(input("Quanto tempo dedicou aos seus hobbies (em minutos)? "))
nivel_energia = int(input("Qual foi o seu nível de energia hoje (de 1 a 5)? "))

print(f"\nData de hoje: {data}")
print(f"Hora que dormiu: {hora_dormiu}")
print(f"Hora que acordou: {hora_acordou}")
print(f"Tempo de tela: {tempo_tela_min} min")
print(f"Tempo para estudos: {estudo_min} min")
print(f"Tempo para hobbies: {hobbies_min} min")
print(f"Nível de energia: {nivel_energia}")


# Confere a existência do arquivo e adiciona as respostas nas colunas
arquivo_existe = os.path.exists("data/rotina.csv")

with open("data/rotina.csv", "a", newline="") as csvfile:
    escritor = csv.writer(csvfile)
    if not arquivo_existe:
        escritor.writerow(["data", "hora_dormiu", "hora_acordou", "tempo_tela_min", "estudo_min", "hobbies_min", "nivel_energia"])
    escritor.writerow([data,hora_dormiu,hora_acordou,tempo_tela_min,estudo_min,hobbies_min,nivel_energia])  
print("Registro de hoje salvo!\n")