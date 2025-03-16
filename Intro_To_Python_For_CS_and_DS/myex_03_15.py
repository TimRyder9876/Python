# myex_03_15

num = 1

for i in range(1,11):
    den = 1
    for x in range(1,i+1):
       den *= x 
    num += (1/den)
    print('Term',i, 'has sum of', round(num,5))