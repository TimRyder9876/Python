#exercise 5_21 Computer-assisted instructions: reducing student fatigue

#import random module
import random

# initialize variables
number1 = random.randrange(1,9)
number2 = random.randrange(1,9)
value = number1 * number2
game = 'N'
answer = 0

#create response list
response_list = ['Very good!','Nice work!','Keep up the good work!']

#Create random multiplication puzzle and determine is response if correct
while game == 'N':
    print(number1)
    print(number2)
    answer = input('How much is ' +str(number1) + ' times '  + str(number2) +'? ')
    if int(answer) == value:
        number3 = random.randrange(0,3)
        phrase = response_list[number3]
        print(phrase)
        game = 'Y'
    else:    
        print('No. Please try again.')
        game = 'N'