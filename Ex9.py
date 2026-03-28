def Ex9():
    for c in range(1,1000):
        for b in range(1,max(c, 1000-c)):
            a = 1000 - b - c
            if a**2 + b**2 == c**2:
                return a*b*c

print(Ex9())