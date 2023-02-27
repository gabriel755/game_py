import forca
import adivinhacao

print('============================')
print('=== ESCOLHA SEU JOGO =======')
print('============================')

print(" (1) Forca (2) Adivinhação")

jogo = input('Qual jogo?')

jogo = int(jogo)

if(jogo == 1 ):
    print('Jogando forca')
    forca.jogar()
elif( jogo == 2 ):
    print('Jogando adivinhação')
    adivinhacao.jogar()
else:
    print('Opção inválida')