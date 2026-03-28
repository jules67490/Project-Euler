def Ex4():
    res = 0
    for a in range(100,1000):
        for b in range(100,1000):
            if str(a*b) == str(a*b)[::-1]:
                if a*b > res:
                    res = a*b
    return res

print(Ex4())

