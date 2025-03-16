# exercise 3_15 tuples representing invoices

#import itemgetter
from operator import itemgetter

#initalisze list
invoice = ()

#create te invoice table
invoice += ((83, 'Electric sander', 7, 57.98),)
invoice += ((24, 'Power saw', 18, 99.99),)
invoice += ((7, 'Sledge hammer', 11, 21.50),)
invoice += ((77, 'Hammer', 76, 11.99),)
invoice += ((39, 'Jig saw', 3, 79.50),)


for i in invoice:
    print(i)

#create new invoice list. tuple cannot be sorted
newInvoice = []

for i in invoice:
    #print(i[1], i[3])
    invline = ((i[1],i[2]*i[3]))
    #print(invline)
    newInvoice += (invline,)

newInvoice.sort(key = itemgetter(1))

total = 0
# using stanard for loop with if for the filter
for i in newInvoice:
    total += i[1]

print(total)
