# Exercicio 1 18:30

a = float(input("Preço do Produto? "))
b = float(input("Percentual de desconto! "))
b2 = b / 100
valor_do_desconto = a * b2
preco_final =  a - valor_do_desconto
print(f" O seu desconto foi de {valor_do_desconto} R$ e o valor final foi de {preco_final} R$, Obrigado pela preferencia. ")