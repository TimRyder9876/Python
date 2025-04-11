# Exercise 5.11 Summarizing letters in a string

import string
# create summarize_letters function
def summarize_letters(istring):
    # Remove spaces and puctuation from the input string
    istring = ''.join(c for c in istring if c.isalpha()).lower()
    print(istring)

    #initialize the frequency dictionary
    letter_frequency = {}

    #iterate through istring counting the letter frequencies
    for char in istring:
        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] =1
    
    #create the tuple for letters and frequencies
    letter_freq_list = list(letter_frequency.items())

    #sort the list
    letter_freq_list.sort()

    #check if the list has all letters of the alphabet
    alphabet_set = set(string.ascii_lowercase)
    string_Set = set(istring)
    has_all_letters = alphabet_set.issubset(string_Set)

    for char, freq in letter_freq_list:
        print(f'{char}: {freq}')

    if has_all_letters:
        print('The string does contain all the letters in the alphabet')
    else:
        print('The string does not contain all the letters of the alphabet')



text = 'abcdefghijklmnopqrstuvwxyz'
istring = text
test = summarize_letters(istring)
