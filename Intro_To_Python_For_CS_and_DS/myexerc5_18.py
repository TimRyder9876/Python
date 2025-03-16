#exercise 5_18 summaing triples of the even integers 2 through 10

list1 = [1,2,3,4,5,6,7,8,9,10]

results = list(map(lambda x: x**3,
               filter(lambda x: x%2 == 0, list1)))

print(results)
x = sum(results)
print(x)

results2 = [item ** 3 for item in list1 if item % 2 == 0]
print(results2)
y = sum(results2)
print(y)