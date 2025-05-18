# Definição da classe Calculadora
class Calculadora:
    def __init__(self):
        # Inicializa o resultado como 0
        self.resultado = 0
        # Cria uma lista para armazenar o histórico de operações
        self.historico = []
        # Define a variável que controla a continuidade do programa
        self.continuar = True

    def calcular(self, entrada):
        # Se o usuário digitar '=', o programa para
        if entrada == "=":
            self.continuar = False  # Define que a execução deve parar
            return self.resultado  # Retorna o último resultado

        try:
            # Avalia a expressão digitada pelo usuário e aplica ao resultado anterior
            self.resultado = eval(f"{self.resultado}{entrada}")
            # Adiciona a operação ao histórico
            self.historico.append(f"{entrada} = {self.resultado}")
            return self.resultado  # Retorna o resultado atualizado
        except Exception as e:
            # Caso ocorra um erro, retorna uma mensagem informando o problema
            return f"Erro: {e}"

    def mostrar_historico(self):
        # Exibe o histórico de todas as operações realizadas
        print("\nHistórico de operações:")
        for operacao in self.historico:
            print(operacao)  # Imprime cada operação armazenada na lista de histórico

# Criação de uma instância da classe Calculadora
calc = Calculadora()
print("Calculadora iniciada. Digite operações ou '=' para finalizar.")

# Loop para manter a calculadora funcionando até que o usuário queira parar
while calc.continuar:
    entrada = input("Digite a operação: ")  # Solicita uma entrada do usuário
    resultado = calc.calcular(entrada)  # Processa a entrada
    print("Resultado:", resultado)  # Exibe o resultado da operação

# Após a finalização, exibe o histórico completo das operações
calc.mostrar_historico()