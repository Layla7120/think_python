def histogram(s):
    d = dict()
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d: 
        val = d[key]
        inverse.setdefault(val,[])
        inverse[val].append(key)
    return inverse


hist = histogram('parrot')
inverse = invert_dict(hist)
print(inverse)