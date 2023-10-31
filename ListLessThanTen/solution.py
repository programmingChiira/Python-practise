a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# basic problem:
for x in a:
    if x< 5: print(x)

# combine challenges 1 and 2:
print( [ x for x in a if x<5 ] )