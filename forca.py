import random

def jogar_forca():

    greetings()

    print("Escolha a categoria: (paises) (frutas)")
    choose = input()
    categorie = choose_categorie(choose)

    secret_word = load_secret_word(categorie)
    list_of_words = []
    mistakes = 0

    print(len(secret_word), "letras:")

    list_of_words = start_correct_letters(secret_word)

    print_list(list_of_words)

    win = False
    died = False

    while(not win and not died): 

        guess = what_is_the_word()

        if(guess in secret_word):
            correct_letter(secret_word, guess, list_of_words)
        else:
            mistakes += 1
            draw_body(mistakes)

        print_list(list_of_words)

        died = mistakes == 7
        win = "_" not in list_of_words

        if(win):
            win_message()
        elif(died):
            loose_message(secret_word)


def greetings(): 
    print("********************************")
    print("Bem vindo ao jogo da forca")
    print("********************************")

def choose_categorie(categorie):
    if(categorie == "paises"):
        return "paises.txt"
    elif(categorie == "frutas"):
        return "frutas.txt"
    

def load_secret_word(categorie):
    with open(categorie, "r", encoding="UTF-8") as f:
        secret_word = f.read().splitlines()

    return random.choice(secret_word).lower()

def start_correct_letters(secret_word):
    return["_" for letters in secret_word]

def what_is_the_word():
    guess = input("Digite uma letra:")
    guess = guess.strip().lower()
    return guess

def correct_letter(secret_word, guess, list_of_words):
    index = 0
    for letters in secret_word:
        if(guess == letters):
            list_of_words[index] = guess
        index += 1

def win_message():
    print("Você ganhou!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def loose_message(secret_word):
    print(f"Você perdeu. A palavra era {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_list(list_of_words):
    for aux in list_of_words:
        print(aux, end="")
    print("")

def draw_body(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    match mistakes:
        case 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
        case 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")
        case 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")
        case 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")
        case 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")
        case 6:
           print(" |      (_)   ")
           print(" |      \|/   ")
           print(" |       |    ")
           print(" |      /     ")

        case 7:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar_forca()