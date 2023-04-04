import random

def jogar_adivinhacao():
    
    greetings()

    random_number = load_random_number()
    min = 1
    max = 100

    level = choose_level()

    try:
        number_of_attempts = define_level(level)

        for aux in range(1, number_of_attempts + 1):
            print(f"Total de tentativas: {number_of_attempts}")
            guess = int(input("Digite um número entre {} e {}: ".format(min, max)))

            if(guess == random_number):
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

def greetings():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")
    print("")

def load_random_number():
    return random.randrange(1,101)

def choose_level():
    print("Escolha o nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil (4) Impossível")
    level = int(input())
    print("")

    return level

def define_level(level):
    match level:
            case 1:
                number_of_attempts = 7
                return number_of_attempts
            case 2:
                number_of_attempts = 5
                return number_of_attempts
            case 3:
                number_of_attempts = 3
                return number_of_attempts
            case 4:
                number_of_attempts = 1
                return number_of_attempts
            case _:
                return "Por favor, selecione um número entre 1 a 4 que corresponda a dificuldade"

if(__name__ == "__main__"):
    jogar_adivinhacao()