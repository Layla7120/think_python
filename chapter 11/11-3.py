known = {'0.1' : 2, '1.0': 2 }
def ack(m, n):
    key = str(m)+"."+str(n)
    if key in known:
        return known[key]
    elif m == 0:
        known[key] = n + 1
        return n + 1
    elif m > 0 and n == 0:
        known[key] = ack(m - 1, 1)
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        known[key] = ack(m - 1, ack(m, n - 1))
        return ack(m - 1, ack(m, n - 1))
    return 


print(ack(13,5))
print(known)