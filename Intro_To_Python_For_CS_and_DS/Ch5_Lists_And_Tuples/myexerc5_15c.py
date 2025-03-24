# exercise 3_15 tuples representing invoices

#import itemgetter
from operator import itemgetter

#initalisze list
invoice = ()

#create te invoice table
invoice += ((83, 'Electric sander', 7, 57.98),)
invoice += ((24, 'Power saw', 19, 99,99),)
invoice += ((7, 'Sledge hammer', 11, 21.50),)
invoice += ((77, 'Hammer', 76, 11.99),)
invoice += ((39, 'Jig saw', 3, 79.50),)


for i in invoice:
    print(i)

#create new invoice list. tuple cannot be sorted
newInvoice = []

for i in invoice:
    print(i[1], i[2])
    invline = ((i[1],i[2]))
    print(invline)
    newInvoice += (invline,)

newInvoice.sort(key = itemgetter(1))

print(newInvoice)
