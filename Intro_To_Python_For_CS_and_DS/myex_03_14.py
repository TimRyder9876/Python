# myex_03_14.py

from decimal import Decimal

const = Decimal('4')
y = 1
sign = 1
x = (1*(const/y))

# print(x)
# print(f'{x:.2f}')

while round(x,3) != Decimal('3.141'):
# print(f'{x:.2f}')
    y +=2
# print(y)
    sign += 1
# print(sign)
# print(const/y)
    if sign%2 == 0:
        x += -1*(const/y)
    else:
        x += const/y    
print(round(x,3))
print(sign)



