# exercise 3_15 tuples representing invoices

#import itemgetter
from operator import itemgetter

#initalisze list
invoice = []

#create te invoice table
invoice.append((83, 'Electric sander', 7, 57.98))
invoice.append((24, 'Power saw', 19, 99,99))
invoice.append((7, 'Sledge hammer', 11, 21.50))
invoice.append((77, 'Hammer', 76, 11.99))
invoice.append((39, 'Jig saw', 3, 79.50))

print('\nBefore sorting:')
for inv in invoice:
    print(inv)
print('\nAfter sorting:')

invoice.sort(key = itemgetter(0))
for inv in invoice:
    print(inv)
