def gameStart():
    while True:
        play = input('do you want to play (y - n)?')
        if play.lower() == 'y':
            print(f'you press {play}')
            print('the game has just started')
            break
        elif play.lower() == 'n':
            print('ok you dont want to play bye!')
            break
        else:
            print('press (y OR n) only!!')
            
def printGame(name):
    name = input('whats your name: ')
    print(f'my name is {name}')
    
    
gameStart()
printGame('ralph')