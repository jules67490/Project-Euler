def Ex2():
    res = 2
    a,b = 1,2
    while b < 4000000:
        b,a = b+a,b
        if b%2 == 0:
            res += b
    return res

print(Ex2())

