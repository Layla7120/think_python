fin = open('words.txt')


def find(word):
    count = 0
    if len(word) > 5:
        for a in range(len(word) - 5):
            # print(word[a] == word[a + 1], a)
            if word[a] == word[a + 1]:
                a += 2
                # print(word[a] == word[a + 1], a)
                if word[a] == word[a + 1]:
                    a += 2
                    # print(word[a] == word[a + 1], a)
                    if word[a] == word[a + 1]:
                        return True
    return False

def counting():
    count = 0
    for line in fin:
        word = line.strip()
        # print(word, "end") 
        if find(word):
            print(word)
    return 
    
counting()