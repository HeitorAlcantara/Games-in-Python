import adivinhacao
import forca

print("")
print("Escolha o jogo que deseja jogar:")

print("(1) Adivinhação (2) Forca")
choose = int(input())

if(choose == 1):
    print("Jogando Adivinhação")
    print("")
    adivinhacao.jogar_adivinhacao()
else:
    print("Jogando forca")
    print("")
    forca.jogar_forca()

