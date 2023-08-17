import random

response = "y"

while response == "y":
    # Simula o lançamento do dado
    number = random.randint(1, 6)
    
    # Imprime o resultado do lançamento do dado
    print("Resultado do lançamento: ", number)
    
    # Pergunta ao usuário se deseja continuar jogando
    response = input("Deseja jogar novamente? (y/n): ")
    
    # Valida a entrada do usuário para garantir que seja 'y' ou 'n'
    while response != "y" and response != "n":
        print("Entrada inválida. Por favor, digite 'y' para continuar ou 'n' para sair.")
        response = input("Deseja jogar novamente? (y/n): ")

print("Obrigado por jogar!")
