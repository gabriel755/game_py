def jogar():
    print('==================================')
    print('=== Bem vindo ao jogo da Forca! ==')
    print('==================================')

    # Secret in plain text for fork game.
    secret_key = "Teste"
    
    # Game conditions var.
    hanged = False
    win_g = False
    
    # While not hanged and not win the game/(True and True).
    while(not hanged and not win_g):
        
        # User attempt.
        letter_in = input('Qual a letra que quer chutar? ')
        letter_in = letter_in.strip()
        
        # Var for show position on secret
        index = 0
        
        # Search user's attempt on secret.
        for letter_srch in secret_key:
            if(letter_in.upper() == letter_srch.upper()):
                print('Encontrada a letra {} na posição {}'.format(letter_in,index))
            index = index + 1
            
if(__name__ == '__main__'):
    jogar()