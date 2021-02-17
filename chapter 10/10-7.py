def has_duplicates(t):
    t = list(t)
    for a in t:
        new = t[:]
        new.remove(a)
        if a in new:
            return True
    return False

print(has_duplicates("avocado"))
print(has_duplicates("pencil"))