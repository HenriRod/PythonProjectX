# Exercicio 3 28:37

# dar input para receber uma frase
frase = input(" Digite uma frase")

# Saber o tamanho da frase. logo usa o "len"
tam = len(frase)

# para pegar a metade da string: vamos pegar o tamanho dividido por dois MAS pode vir um numero quebrado com virgula. assim definimos a variavel "int" para pegar o numero inteiro anterior. assim podemos ir do inicio até o meio mas com um numero inteiro.
frase2 = frase[0:int(tam/2)]

# agora temos outra coisa.... podemos definir para pegar ao contrario e para isso usamos o sinal "-" porque não sabemos quantos numeros vai haver e como o exercicio pede os dois ultimos até o meio logo faz mais sentido ir de tras para frente e só pegar o necessario...
print(frase2[-2:])