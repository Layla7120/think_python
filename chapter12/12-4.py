def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower() #소문자로 다 바꾸고 공백 없앤다
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter # '한'자리는 값이라고 생각하는 거
    return d


memo = {}
memo[''] = [''] # 공백 저장하기

def children(s, wordlist):
    l = []
    for w in range(len(s)):
        child = s[: w] + s[w+1:]
        if child in wordlist:
            l.append(child)
    return l

def is_reducible(s, wordlist): #재귀의 정의를 정확하게 알고 있어야 함
    l = []
    if s in memo:
        return memo[s]

    for child in children(s, wordlist):
        if is_reducible(child, wordlist):
            l.append(child)

    memo[s] = l
    return l

def all_reducible(wordlist):
    res = []
    for word in wordlist:
        t = is_reducible(word, wordlist)
        if t != []:
            res.append(word)
    return res

def print_longest_words(wordlist):
    words = all_reducible(wordlist)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse = True) #오름차순으로 정렬 reverse = True

    for _, word in t[0:5]:
        organize_print(word)
        print('\n')

def organize_print(word):
    if len(word) == 0:
        return
    print(word, end = ' ')
    t = is_reducible(word, wordlist)
    organize_print(t[0])
    


if __name__ == "__main__":
    wordlist = make_word_dict()
    # print(all_reducible(wordlist)) #확인
    print_longest_words(wordlist)