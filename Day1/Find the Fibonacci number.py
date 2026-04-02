import math

def Fibonacci(x):
    arr = [0, 1]
    for i in range(2, x):
        arr.append(arr[i-1] + arr[i-2])
    return arr[x-1]

print(Fibonacci(10))
print(Fibonacci(20))