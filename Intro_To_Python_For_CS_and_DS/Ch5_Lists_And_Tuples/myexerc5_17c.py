# exercise 5_17 map performance

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def squares(numbers):
    counter1 = 0
    counter2 = 0
    for x in numbers:
        number2 = x % 2
        counter1 += 1 
        print(f'Original number:{x}')
        if number2 != 0:
            x = x ** 2
            counter2 += 2
            print(f'Squared number:{x}')
    print(f'Lambda map counter: {counter1}')
    print(f'Filter counter: {counter2}')
squares(numbers)            

