def chop(t):
    del t[0], t[len(t) - 1]
    return 

t = [1, 2, 3, 4]
print(chop(t), t)