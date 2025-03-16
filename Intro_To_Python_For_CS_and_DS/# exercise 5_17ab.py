# exercise 5_17 map performance

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def filter_function(numbers):
    print('Filter function with:', numbers)
    return numbers % 2 !=0

def square_function(numbers):
    print('Square function with:', numbers)
    return x ** 2

results = list(map(square_function,
                   filter(filter_function,numbers)))
