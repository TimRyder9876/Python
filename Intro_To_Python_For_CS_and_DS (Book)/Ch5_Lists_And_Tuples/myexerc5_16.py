#exercise 5_16 sorting letters and removing duplicates

#import random module
import random
import numpy as np

#create the letter dictionary
letterkey = {1:'a', 2:'b', 3:'c',
             4:'d', 5:'e', 6:'f'}

#initialize letters list
list1 = []

#randomly select 20 numbers and then get the corresponding letter A to F
for i in range(20):
    numbers = random.randrange(1,7)
    letters = letterkey.get(numbers,'')
    list1.append(letters)

#sort the list of  ascending
list1.sort()
print(list1)

#sort the list of  descending
list1.sort(reverse=True)
print(list1)


values = np.unique(list1)
values.sort()
print(values)
