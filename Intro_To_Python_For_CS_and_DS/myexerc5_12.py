#exercise 5_12 telephone number generator

# Define all numbers to letters dictionary
number_list = {'2':'ABC',
               '3':'DEF',
               '4':'GHI',
               '5':'JKL',
               '6':'MNO',
               '7':'PRS',
               '8':'TUV',
               '9':'WXY'}

#Create function to generate all possible word combinations from a number
def generate_word_combination(phone_number):
    
    #initialize a list for the word combinations
    word_combos = ['']

    # Iterate through each number in phone number
    for digit in phone_number:
        #Get the letters corresponding to the digit
        letters = number_list.get(digit,'')

        #Generate new combinations by combining the existing ones with the letters
        new_combinations = []
        for combo in word_combos:
            for letter in letters:
                new_combinations.append(combo + letter)
        word_combos = new_combinations
    
    return word_combos

phone_number = '3272625'
combinations = generate_word_combination(phone_number)
print('Word combinations for phone number', phone_number,':')
for word in combinations:
    #print(word)
    print(f'{word}', end='  ')

