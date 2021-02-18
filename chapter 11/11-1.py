def dictionary(f):
    d = dict()
    count = 0
    for line in f:
        line = line.strip()
        d[line] = count
        count += 1
    return d    


fin = open('test.txt')

d = dictionary(fin)
print(d)
# if 'retunes' in d:
#     print(d['retuned'])
