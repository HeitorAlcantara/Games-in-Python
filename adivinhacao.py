import random as Random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")
print("")


random_number = Random.randrange(1,101)
min = 1
max = 100

print("Escolha o nível de dificuldade:")
print("(1) Fácil (2) Médio (3) Difícil (4) Impossível")
level = int(input())
print("")

try:
    match level:
        case 1:
            number_of_attempts = 7
        case 2:
            number_of_attempts = 5
        case 3:
            number_of_attempts = 3
        case 4:
            number_of_attempts = 1
        case _:
            print("Por favor, selecione um número entre 1 a 4 que corresponda a dificuldade.")

    for aux in range(1, number_of_attempts + 1):
        print(f"Total de tentativas: {number_of_attempts}")
        guess = int(input("Digite um número entre {} e {}: ".format(min, max)))

        if guess == random_number:
            print("Voce acertou!!")
            break
        elif(guess > random_number):
            print("Você errou! O número secreto é menor.")
        else:
            print("Você errou! O número secreto é maior.")

        number_of_attempts -= 1
except Exception as err: 
    print(f"Unexpected {err}")

print("Fim do jogo.","\n","O número secreto era:", random_number)