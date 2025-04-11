# my esxercises 6_10

#{'red', 'green','blue'}
#{'cyan','green','blue','magenta','red'}

# Is everything on the left the same thing as on the right?
x = {'red', 'green','blue'}=={'cyan','green','blue','magenta','red'}
print(x)

#Is everything on the left not the same thing as on the right?
x = {'red', 'green','blue'}!={'cyan','green','blue','magenta','red'}
print(x)

# Is everything on the left within the right side and the sets are not equal?
x = {'red', 'green','blue'}<{'cyan','green','blue','magenta','red'}
print(x)

# Is everything on the left within the right side and the sets might be equal?
x = {'red', 'green','blue'}<={'cyan','green','blue','magenta','red'}
print(x)

# is everything on the right side in the left side and the sets are not equal?
x = {'red', 'green','blue'}>{'cyan','green','blue','magenta','red'}
print(x)

# is everything on the right side in the left side and the sets might be equal?
x = {'red', 'green','blue'}>={'cyan','green','blue','magenta','red'}
print(x)

# combine the sets into one set
x = {'red', 'green','blue'}|{'cyan','green','blue','magenta','red'}
print(x)

# find the intersections of the two sets
x = {'red', 'green','blue'}&{'cyan','green','blue','magenta','red'}
print(x)

# find the sets on the left side that are not in the right side
x = {'red', 'green','blue'}-{'cyan','green','blue','magenta','red'}
print(x)

# find the set where values of one are not in the other and vice versa
x = {'red', 'green','blue','black'}^{'cyan','green','blue','magenta','red'}
print(x)