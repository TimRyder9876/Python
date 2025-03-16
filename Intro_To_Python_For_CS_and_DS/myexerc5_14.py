#exercise 5_!4 is sequence sorted

#get input
#compare original string vs a sorted string
#if both strings are equal, return True that string is sorted
def is_sorted(get_sequence):
    list1 = []
    list1 += get_sequence
    list2 = sorted(list1)

    print(list1)
    print(list2)
    if list1 == list2:
        print('Sequence is sorted.')
    else:
        print('Sequence is not sorted')

get_sequence = [123645]
is_sorted(get_sequence)