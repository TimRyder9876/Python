import random 


game = 'Y'

while game.upper() == 'Y':
    x = random.randrange(1,1000)
    guesses = 0
    print(x)
    number1 = 0
    while number1 != x:
        number1 = int(input('Guess my number from 1 t0 1000: '))
        guesses += 1
        if number1 > x:
            print('Too high. Try again.')
        elif number1 < x:
            print('Too low. Try again.')    
        else: 
            print('Congratulations. You guessed the number!')
            if guesses <= 10:
                print('Either you know the secret or you got lucky!')
            else:
                print('You should be able to do better!')    
            game = input('Do you want to play again? Y/N/')

