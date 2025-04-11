# myex_03_11.py

# initialize 
from decimal import Decimal
tot_miles = 0
tot_gallons = 0
gallons = 0
avg_trip = 0

# processing
gallons = float(input('Enter the gallons used: '))

while gallons != -1:
    tot_gallons += gallons
    miles = float(input('Enter the miles driven: '))
    tot_miles += miles
    avg_trip = miles/gallons
    print(f'The miles/gallon for this trip was {avg_trip:.6f}')
#   print(f'The miles/gallon for this trip was, {avg_trip:.5f}')
    gallons = float(input('Enter the gallons used: '))

print('The overall average miles/gallon was', tot_miles/tot_gallons)

