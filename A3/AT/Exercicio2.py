# input com nome e um com idade
nome = input("Digite seu nome! ")
idade = int(input("Digite sua idade"))

if nome == "Henrique":
    print(f"Bem vindo {nome}")
elif idade < 18:
    print("Acesso negado para menores de idade")
elif idade >= 100:
    print("Voce provavelmente não tem essa idade!")