# fig 03_10_03.py
""" Class average prgram with sequence-controlled repetition"""

# initialization phase
total = 0
grade_counter = 0
grades = [98,76,71,87,83,90,57,79,82,94] # list of 10 grades

# processing phase
for number in grades:
    total += number # add current grade to the running total
    grade_counter += 1 # idicate that one more grade was processed

# termination phase
average = total / grade_counter
print(f'Class average is {average}')