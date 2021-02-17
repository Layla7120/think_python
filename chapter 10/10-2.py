def cumsum(t):
    total = 0
    for a in range(len(t)):
        total += t[a]
        t[a] = total
    return t

t = [1, 2, 3]
print(cumsum(t))

