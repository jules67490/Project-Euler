import numpy as np

def is_prime(n, prime_list):
    for i in prime_list:
        if n%i == 0:
            return False
    return True

def Ex7(n):
    prime_list = []
    number_to_test = 2
    while len(prime_list) <= n-1:
        
        if is_prime(number_to_test, prime_list):
            
            prime_list.append(number_to_test)
        number_to_test += 1
    return prime_list[-1]

print(Ex7(10001))