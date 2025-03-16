import random

number1 = random.randrange(1,9)
number2 = random.randrange(1,9)
value = number1 * number2
game = 'N'
answer = 0

while game == 'N':
    print(number1)
    print(number2)
    answer = input('How much is ' +str(number1) + ' times '  + str(number2) +'? ')
    if int(answer) == value:
        print('Very good! Nice Work!')
        game = 'Y'
    else:    
        print('No. Please try again.')
        game = 'N'
