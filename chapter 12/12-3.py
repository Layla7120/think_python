def similarity(w1, w2):
    count = 0
    if len(w1) == len(w2):
        for a in range(len(w1)):
            if w1[a] == w2[a]:
                count += 1
            
    if count == len(w1) - 2:
        return True
    return False

def sorted_string(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """애너그램을 찾으면 계속 추가하는 함수"""
    d = {}
    a = []
    for line in open('words.txt'):
        word = line.strip().lower()
        t = sorted_string(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)

    for v in d.values():
        if len(v) > 1:
            a.append(v)
    return a

def converse_words(t):
    for line in t:
        if range(len(line)) == 2:
            if similarity(line[0], line[1]):
                print(line[0], line[1])
        else:
            line.sort()
            for a in range(len(line) - 1):
                if similarity(line[a], line[a + 1]):
                    print(line[a], line[a + 1])

if __name__ == '__main__':
    # print(similarity("converse", "conserve"))
    # print(all_anagrams("test.txt"))
    print(converse_words(all_anagrams("test.txt")))