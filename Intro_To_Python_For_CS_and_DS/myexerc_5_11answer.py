import string

def summarize_letters(input_string):
    # Remove spaces and punctuation from the input string and convert it to lowercase
    input_string = ''.join(c for c in input_string if c.isalnum()).lower()  


    # Initialize a dictionary to store the frequencies of each letter
    letter_frequency = {}
    
    # Iterate through the characters in the cleaned string
    for char in input_string:
        # Increment the frequency count for each letter
        letter_frequency[char] = letter_frequency.get(char, 0) + 1
    
    # Convert the dictionary to a list of tuples
    letter_frequency_list = list(letter_frequency.items())
    
    # Sort the list by the letter (optional)
    letter_frequency_list.sort()
    
    return letter_frequency_list

# Input from the user
user_input = input("Enter a string: ")

# Call the function and display the results
result = summarize_letters(user_input)

# Output the letter frequencies
for letter, frequency in result:
    print(f"'{letter}': {frequency}")

# Check if the string contains all the letters of the alphabet
alphabet = set(string.ascii_lowercase)
input_set = set(letter.lower() for letter, _ in result)
if alphabet.issubset(input_set):
    print("The string contains all the letters of the alphabet.")
else:
    print("The string does not contain all the letters of the alphabet.")