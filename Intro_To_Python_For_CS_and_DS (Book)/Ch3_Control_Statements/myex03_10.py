# my03_10.py

from decimal import Decimal

principal = Decimal('1000')
rate = Decimal('0.07')


for number  in range(31):
    interest = principal*(1+rate)**number
    print(f'{number} {interest:.2f}')
