# Registro diário de rotina
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


# Pede um número inteiro dentro de um intervalo e devolve o valor
def pedir_numero(pergunta, minimo=0, maximo=1440):
    while True:
        resposta = input(pergunta)
        try:
            numero = int(resposta)
            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Formato inválido! Digite um número inteiro.")

# Faz as perguntas do dia e devolve um dicionário com as respostas
def perguntar_dados():
    data = datetime.date.today()
    hora_dormiu = pedir_hora("Que horas você dormiu (HH:MM)? ")
    hora_acordou = pedir_hora("Que horas você acordou (HH:MM)? ")
    tempo_tela_min = pedir_numero("Qual foi o seu tempo de tela (em minutos)? ", 0, 1440)
    estudo_min = pedir_numero("Por quanto tempo você estudou (em minutos)? ", 0, 1440)
    hobbies_min = pedir_numero("Quanto tempo dedicou aos seus hobbies (em minutos)? ", 0, 1440)
    nivel_energia = pedir_numero("Qual foi o seu nível de energia hoje (de 1 a 5)? ", 1, 5)
    return {'data': data, 'hora_dormiu': hora_dormiu, 'hora_acordou': hora_acordou, 'tempo_tela_min': tempo_tela_min, 'estudo_min': estudo_min, 'hobbies_min': hobbies_min, 'nivel_energia': nivel_energia}


# Recebe o registro e imprime o resumo
def mostrar_resumo(dados):
    print(f"\nData de hoje: {dados['data']}")
    print(f"Hora que dormiu: {dados['hora_dormiu']}")
    print(f"Hora que acordou: {dados['hora_acordou']}")
    print(f"Tempo de tela: {dados['tempo_tela_min']} min")
    print(f"Tempo para estudos: {dados['estudo_min']} min")
    print(f"Tempo para hobbies: {dados['hobbies_min']} min")
    print(f"Nível de energia: {dados['nivel_energia']}")


# Confere a existência do arquivo e adiciona as respostas nas colunas
def salvar_registro(dados):
    arquivo_existe = os.path.exists("data/rotina.csv")
    with open("data/rotina.csv", "a", newline="") as csvfile:
        escritor = csv.writer(csvfile)
        if not arquivo_existe:
            escritor.writerow(["data", "hora_dormiu", "hora_acordou", "tempo_tela_min", "estudo_min", "hobbies_min", "nivel_energia"])
        escritor.writerow([dados['data'],dados['hora_dormiu'],dados['hora_acordou'],dados['tempo_tela_min'],dados['estudo_min'],dados['hobbies_min'],dados['nivel_energia']])  
    print("Registro de hoje salvo!\n")

dados = perguntar_dados()
salvar_registro(dados)
mostrar_resumo(dados)