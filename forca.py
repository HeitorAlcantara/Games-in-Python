def jogar_forca():
    print("********************************")
    print("Bem vindo ao jogo da forca")
    print("********************************")

    secret_word = "snAKes".lower()
    list_of_words = []
    mistakes = 0

    print(len(secret_word), "letras:")

    list_of_words = ["_" for letters in secret_word]

    for under_line in list_of_words:
        print(under_line, end="")
    print("")

    win = False
    died = False

    secret_word_list = list(secret_word)

    while(not win and not died):

        guess = input("Digite uma letra:")
        guess = guess.strip().lower()

        if(guess in secret_word):
            index = 0
            for letters in secret_word:
                if(guess == letters):
                    list_of_words[index] = guess
                index += 1
        else:
            mistakes += 1
            print(f"Erros: {mistakes} de 6")

        for correct_letters in list_of_words:
            print(correct_letters, end="")
        print("")

        if(secret_word_list == list_of_words):
            win = True
            print("Você ganhou!!")
        elif(mistakes == 6):
            died = True
            print("Você perdeu.")
        
    

if(__name__ == "__main__"):
    jogar_forca()