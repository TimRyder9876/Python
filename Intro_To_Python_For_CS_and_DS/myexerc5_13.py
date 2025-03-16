#exercise 5_1 Word to phone number generator

# Define all letters to numbers dictionary
number_list = {'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3',
               'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5',
               'M':'6', 'N':'6', 'O':'6', 'P':'7', 'R':'7', 'S':'7',
               'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9'}

#Create function to generate all possible word combinations from a number
def generate_phone_number(word_input):
    
    word_input = word_input.upper()

    #initialize a list for the word-number combinations
    number_combo = ['']

    # Iterate through each letter in word
    for letter in word_input:
        #Get the number corresponding to the letter
        numbers = number_list.get(letter,'')
        #number_combo.append(numbers)
        #Generate new combinations by combining the existing ones with the letters
        new_combinations = []
        for combo in number_combo:
            for number in numbers:
                new_combinations.append(combo + numbers)
        number_combo = new_combinations
    
    return number_combo

word_input = 'bigBird'
combinations = generate_phone_number(word_input)
print('Phone number for Word combinations', word_input,':')
for phone_number in combinations:
    print(f'{phone_number}', end='  ')
