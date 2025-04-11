import random 
x = random.randrange(1,1000)
print(x)
number1 = 0

while number1 != x:
    number1 = int(input('Guess my number from 1 t0 1000: '))
    if number1 > x:
        print('Too high. Try again.')
    elif number1 < x:
        print('Too low. Try again.')    
    else: 
        print('COngratulations. You guess the number!')

print(number1)
