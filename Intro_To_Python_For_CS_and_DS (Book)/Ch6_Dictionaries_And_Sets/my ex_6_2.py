#my ex_6_2
from collections import Counter
text = ('to be or not to be that is the question')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(word, count)