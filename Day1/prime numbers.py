import math

def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

print(prime(100))
print(prime(37))