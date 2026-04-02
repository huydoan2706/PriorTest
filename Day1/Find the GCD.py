def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

print (gcd(120,200))
print (gcd(23, 30))