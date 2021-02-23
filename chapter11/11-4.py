def has_duplicates(t):
    d = {}
    for a in t:
        if a in d:
            return True
        d[a] = True
    return False


print(has_duplicates([1, 2, 3, 4, 8, 5, 6]))
print(has_duplicates(['a','v','pc','a','d','o']))