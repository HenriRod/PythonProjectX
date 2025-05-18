import requests

# Função para obter a cotação de moedas em tempo real
def obter_cotacao(moeda_origem, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    resposta = requests.get(url)
    dados = resposta.json()
    
    chave = f"{moeda_origem}{moeda_destino}"
    if chave in dados:
        return float(dados[chave]["bid"])
    else:
        return None

# Função para converter valores entre moedas
def converter_moeda(valor, moeda_origem, moeda_destino):
    cotacao = obter_cotacao(moeda_origem, moeda_destino)
    if cotacao:
        return valor * cotacao
    else:
        return "Erro ao obter cotação."

# Lista de moedas disponíveis
moedas_disponiveis = ["USD", "EUR", "BRL", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR"]

# Interface do usuário
print("Conversor de Moedas em Tempo Real")
print("Moedas disponíveis:", ", ".join(moedas_disponiveis))

moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()
moeda_destino = input("Digite a moeda de destino (ex: BRL): ").upper()
valor = float(input("Digite o valor a ser convertido: "))

resultado = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"\n{valor} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")