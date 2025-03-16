#ex 5.10 anagram
#Find all combinations of a string input for anagrams

def generate_anagrams(s, start=0):
    if start == len(s) - 1:
        print("".join(s), end=' ')
        print(s)
        return
    
    for i in range(start, len(s)):
        # Swap the characters at indices 'start' and 'i'
        s[start], s[i] = s[i], s[start]
        
        # Recur with the next character
        generate_anagrams(s, start + 1)
        
        # Backtrack: Swap the characters back to their original positions
        s[start], s[i] = s[i], s[start]

# Input string
input_string = "abc"

# Convert the input string to a list of characters for easy manipulation
input_list = list(input_string)

# Generate and print all anagrams
generate_anagrams(input_list)