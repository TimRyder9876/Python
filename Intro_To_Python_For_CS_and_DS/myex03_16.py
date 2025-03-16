# myex03_16.py

# initialize variables
max1 = 0
max2 = -1

for x in range(10):
    num = int(input('Enter number: '))
    if num >= max1:
        max2 = max1
        max1 = num
    elif num >= max2:
        max2 = num
print('The maximum entered values are: ', max1,'and', max2)