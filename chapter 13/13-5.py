def histogram(s):
    d = dict()
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1
    return d

import random
def choose_from_hist(t):
    return random.choice(t)

if __name__ == "__main__":
    t = 'aab'
    hist = histogram(t)
    print(hist)
    print(choose_from_hist(t))
    