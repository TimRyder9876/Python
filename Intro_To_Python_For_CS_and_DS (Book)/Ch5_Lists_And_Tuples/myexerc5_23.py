# exercise 05_23 functional style programming: order of filter and map calls

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

result = list(filter(lambda x: x % 2 == 0,
                     map(lambda x: x * 2, numbers)))

print(result)

result2 = list(map(lambda x: x * 2,
                   filter(lambda x: x % 2 == 0, numbers)))

print(result2)