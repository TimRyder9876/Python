for x in range(10):
    for x2 in range(10):
        # Calculate the farhrenheit value from the celcius input
        f = (9/5) * ((x*10)+ x2) + 32
        print(f'{round(f,0):>8}', end= '')
    print()   