import numpy as np

def Ex3(n):
    res = 0
    for i in range(2,int(np.sqrt(n))+1):
        i_prime = True
        for j in range(2,int(np.sqrt(i))+1):
            if i%j == 0: # non prime
                i_prime = False
        if n%i == 0 and i_prime:
            res = i
    return res

print(Ex3(600851475143))


