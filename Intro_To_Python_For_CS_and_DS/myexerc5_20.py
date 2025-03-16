# exercise 5_20 two=dimensional list in tabulaar format

names = [('John','Jones'),
         ('Fred','Willard'),
         ('Martha','Jones'),
         ('Chris','Smith'),
         ('Jonus','Jones')]

print(names)

def display_table(table):
    #Get the number of rows and columns in the table
    rows = len(table)
    columns = len(table[0] if rows > 0 else 0)

    #Print the column indices as headings
    print('\t', end='')
    for col in range(columns):
        print(col, end='\t')
    print()

    #Print each row with the row index at the left
    for row in range(rows):
        print(row, end='\t')
        for col in range(columns):
            print(table[row][col], end='\t')    
        print()

display_table(names)
