def in_disect(a, t, start, end):
    mid  = (start + end) // 2
    if start <= end:
        if t[mid] == a:
            return mid
        elif t[mid] < a:
            start = mid + 1
            return in_disect(a, t, start, end)
        else:
            end = mid - 1
            return in_disect(a, t, start, end)
    else:
        return
    

fin = open('test.txt')
t = []
for line in fin:
    word = line.strip()
    t = t + [word]
print(in_disect('aals', t, 0, len(t) - 1))
print(in_disect('hello', t, 0, len(t) - 1))
