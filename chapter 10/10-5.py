def is_sorted(t):
    for a in range(len(t)):
        if t[a] > t[a + 1]:
            return False
        return True

print(is_sorted([1, 2, 3]))
print(is_sorted(['b','a']))