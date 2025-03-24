a = 13431
val1 = a//10000
val2 = (a%10000)//1000
val3 = ((a%10000)%1000)//100
val4 = (((a%10000)%1000)%100)//10
val5 = a%10

if val1 == val5 and val2 == val4:
    print('Number is a palindrome')    
print(val1)
print(val2)
print(val3)
print(val4)
print(val5)