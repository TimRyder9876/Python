# my ex 6_5 find duplicate words in sentence
from collections import Counter


sentence= input('Enter sentence to determine words that are duplicated.')
sentence = sentence.lower()


counter = Counter(sentence.split())
for word, count in counter.items():
    if count > 1:
        print(word, count)
