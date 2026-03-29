import numpy as np

def Ex12(limit):
    k = 10
    while True:
        n = int(k*(k+1)/2)
        counter_divisors = 1 # the number itself
        for i in range(1,int(np.sqrt(n))+1):
            if n%i == 0: 
                counter_divisors += 2
            if counter_divisors >= limit:
                return n
        k += 1

print(Ex12(500))