import math

def largest_number(a):
    largest = -math.inf
    for x in a:
        if x > largest:
            largest = x
    return largest

print(largest_number([18,27,84,96,7,81,91]))