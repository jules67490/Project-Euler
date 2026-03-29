import numpy as np

def isprime(n):
    for i in range(2,int(np.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def Ex9(n):
    result = 2+3
    current = 2
    while current < n:
        if current%2 != 0 or current%3 != 0:
            if isprime(current):
                result += current
        current += 1
    return result

print(Ex9(2000000))