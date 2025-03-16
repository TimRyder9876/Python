import random

diflevel = int(input('Enter the difficulty level (1 or 2): '))
if diflevel == 1:
    number1 = random.randrange(1,10)
    number2 = random.randrange(1,10)
else:
    number1 = random.randrange(1,100)
    number2 = random.randrange(1,100)    
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
