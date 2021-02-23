def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def dictionary(f):
    d = dict()
    count = 0
    for line in f:
        line = line.strip()
        d[line] = count
        count += 1
    return d    
def find_rotate():
    fin = open('words.txt')
    d = dictionary(fin)
    for key in d:
        for a in range(1, 13):
            if rotate_word(key, a) in d:
                print(key, a, rotate_word(key, a))
                return True
    return False
if __name__ == '__main__':
    print(find_rotate())




