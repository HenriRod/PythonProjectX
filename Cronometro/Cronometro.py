import time

def temporizador(segundos, mensagem):
    while segundos:
        minutos, segundos_restantes = divmod(segundos, 60)
        print(f"\r{mensagem}: {minutos:02}:{segundos_restantes:02}", end="")
        time.sleep(1)
        segundos -= 1
    print(f"\n{mensagem} concluído!")

def pomodoro(ciclos=4, trabalho=25, descanso=5):
    print("Iniciando Técnica Pomodoro!")
    for ciclo in range(1, ciclos + 1):
        print(f"\nCiclo {ciclo}/{ciclos}")
        temporizador(trabalho * 60, "Tempo de foco")
        if ciclo < ciclos:
            temporizador(descanso * 60, "Tempo de descanso")
    print("\nTodos os ciclos concluídos! Boa produtividade!")

# Configuração do usuário
ciclos = int(input("Quantos ciclos deseja realizar? "))
tempo_trabalho = int(input("Tempo de trabalho (minutos): "))
tempo_descanso = int(input("Tempo de descanso (minutos): "))

# Executa o Pomodoro
pomodoro(ciclos, tempo_trabalho, tempo_descanso)