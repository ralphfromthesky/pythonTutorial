lives = 3
while True:
    print('whats my name?')
    name = input('your name: ')
    if name == 0:
        print('game over')
        break
    if name != 'ralph':
        lives -= 1
        print(f'Wrong! you only have {lives} lives left')
        if lives == 0:
            print('game over')
            break

    else:
        print('correct')
        break
    
