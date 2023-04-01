import random as Random
import math as Math

print("Bem vindo ao jogo de adivinhação")
print("******************************")


random_number = Math.floor(Random.random() * 10)
number_of_attempts = 3


while(number_of_attempts > 0):
    print(f"Total de tentativas: {number_of_attempts}")
    guess = int(input("Digite um número entre 1 e 10: "))
    if guess == random_number:
        print("Voce acertou!!")
        break
    elif(guess > random_number):
        print("Você errou! O número secreto é menor.")
    else:
        print("Você errou! O número secreto é maior.")
    number_of_attempts -= 1
print("Fim do jogo.","\n","O número secreto era:", random_number)