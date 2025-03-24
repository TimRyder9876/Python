# my exercice 6_8

hundreds_digit = {1:'One Hundred',2:'Two Hundred', 3: 'Three Hundred',
            4: 'Four Hundred', 5: 'Five Hundred', 6: 'Six Hundred',
            7: 'Seven Hundred', 8: 'Eight Hundred', 9: 'Nine Hundred'}

tens_digit = {2: 'Twenty',3: 'Thirty',4: 'Forty',5:'Fifty', 6:'Sixty',
              7: 'Severnty', 8:'Eighty', 9:'Ninety'}

tens_numbers = {10: 'ten', 11: 'Eleven', 12: 'Twelve',13: 'Thirteen', 14:'Fourteen',
               15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
               18: 'Eighteen', 19: 'Nineteen'}

single_digit = {1: 'One', 2: 'Two', 3:'Three', 4:'Four', 5:'Five',
                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

number = 123.43

print(number)

hundreds = number // 100
tens = int(number-hundreds*100)
tenths = (number - (hundreds*100))// 10
digits = (int(number) -(hundreds*100) - (tenths*10))

#print(hundreds) 
#print(tens)
#print(tenths)
#print(digits)
x = hundreds_digit.get(hundreds)
y = tens_numbers.get(tens,'N')
z1 = tens_digit.get(tenths,'')
z2 = single_digit.get(digits,'')

print(x)
text = x + ' '
if y != 'N':
    print(y)
    text += Y + ' '
else:
    print(z1)
    print(z2)
    text += z1 + '-' + z2 + ' '

print(text)
