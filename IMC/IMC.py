# Importa a biblioteca necessária para pausar a execução (opcional)
import time

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para fornecer dicas de saúde com base no IMC
def obter_classificacao_e_dicas(imc):
    if imc < 18.5:
        return ("Abaixo do peso", "Procure manter uma alimentação equilibrada e rica em nutrientes.")
    elif 18.5 <= imc < 24.9:
        return ("Peso normal", "Continue com um estilo de vida saudável e exercícios regulares.")
    elif 25 <= imc < 29.9:
        return ("Sobrepeso", "Tente manter uma dieta balanceada e pratique atividades físicas regularmente.")
    else:
        return ("Obesidade", "Consulte um profissional de saúde para orientações sobre hábitos saudáveis.")

# Entrada do usuário
print("Calculadora de IMC – Índice de Massa Corporal")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Obtém classificação e dicas
classificacao, dica = obter_classificacao_e_dicas(imc)

# Exibe os resultados
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Dica de saúde: {dica}")

# Pequena pausa para melhor visualização dos resultados (opcional)
time.sleep(2)