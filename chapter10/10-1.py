def nested_sum(t):
    total = 0
    for a in range(len(t)):
        total += sum(t[a])
    return total

a = [[1,2],[3],[4,5,6]]
print(nested_sum(a))


