# myex03_08


number = int(input('Enter integer: '))
min = number
max = number
cnt = 1
total = number
product = number

for i in range(1,4):
    number = int(input('Enter integer: '))
    total += number
    cnt += 1
    product *= number
    if min > number:
        min = number
    if max < number:
        max = number    

print('Sum is', total)
print('Average is', total/cnt)
print('Product is', product)
print('Min is', min)
print('Max is', max)
