# me_fig_03_03.py
""" Using nested control statements to analyze examination results"""

# initialize variables
passes = 0
failures = 0
i = 0

# process 10 students
while i != 10:
    # get one exam result
    result = int(input("Enter result 1=Pass, 2=Fail: "))
    if result not in (1,2):
        continue

    elif result == 1:
         passes += 1

    else:
        failures += 1
    i += 1
# termination phase
print('Passed:', passes)
print('Failures:', failures)

if passes > 8:
    print('Bonus to instructor')