def Ex5():
    '''This can be done by hand. We need to multiply:
    - The prime numbers between 1 and 20: 2, 3, 5, 7, 11, 13, 17, 19 (8 numbers already)
    - By multiplying these numbers, we already have 6, 10, 14, 15 (+ 4 = 12)
    - An additional 2 to have 4, 12 and 20 (+ 3 = 15)
    - An additional 3 to have 9 and 18 (+ 2 = 17)
    - An additional 2 to have 8 (+ 1 = 18). 
    - An additional 2 to have 16 (+ 1 = 19). Adding 1, and number created by the multiplication of all the previous ones will be the smallest evenly divisible by all number from 1 to 20'''
    return 2*2*2*2*3*3*5*7*11*13*17*19

print(Ex5())