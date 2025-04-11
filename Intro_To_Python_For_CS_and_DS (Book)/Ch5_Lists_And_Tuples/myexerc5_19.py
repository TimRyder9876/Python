# exercise 5_19 finding peope with a specified last name

names = [('John','Jones'),
         ('Fred','Willard'),
         ('Martha','Jones'),
         ('Chris','Smith'),
         ('Jonus','Jones')]

print(names)

searches = list((filter(lambda x: x[1] == 'Jones',names )))
print(searches)