my_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
           10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
           15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
           19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
           50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
           90: 'Ninety'}

amount = float(input("Enter the amount: "))

if amount < 1000:
    amount_str = str(amount)
    temp = int(amount)
    hundred = int(temp / 100)
    sentence = ""
    
    if hundred > 0:
        sentence += my_dict[hundred].upper() + ' HUNDRED '
    
    val = (temp % 100)
    
    if val >= 1 and val <= 19 or val % 10 == 0:
        sentence += my_dict[val].upper()
    else:
        sentence += my_dict[int(val / 10) * 10].upper() + " " + my_dict[(val % 10)].upper()
    
    if (amount - temp) != 0:
        index = amount_str.find('.')
        a = amount_str[index + 1:]
        b = pow(10, len(a))
        sentence += " " + a + "/" + str(b)
    
    print(sentence)
else:
    print("Amount is not less than 1000")