

def interlock(word1, word2):
    return len(word1)== len(word2) or abs(len(word1) - len(word2)) == 1
        
        

def interlock_three(word1, word2, word3):
    len_w1 = len(word1) 
    len_w2 = len(word2) 
    len_w3 = len(word3) 
    len_ary = [len_w1,  len_w2, len_w3]
    len_ary.sort()
    return abs(len_ary[0] - len_ary[2]) <= 1
        
def interlock_find(t):
    for a in range(len(t)):
        for b in range(a + 1, len(t)):
            if interlock(t[a], t[b]):
                return True
    return False

def interlock_three_find(t):
    for a in range(len(t)):
        for b in range(a + 1, len(t)):
            for c in range(b + 1, len(t)):
                if interlock_three(t[a], t[b],t[c]):
                    return True
    return False


print(interlock('shoe', 'cold'))
print(interlock_three('shoe', 'cold','hello'))

fin = open('test.txt')
t = []
for line in fin:
    word = line.strip()
    t = t + [word]

print(interlock_find(t))
