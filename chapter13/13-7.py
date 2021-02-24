import string
from random import randint

def cumsum(t):
    total = 0
    for a in range(len(t)):
        total += 1
    return total

def process_file(filename):
    hist = dict()
    fp = open(filename, encoding= 'utf-8')
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line,hist):
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

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
        return end + 1
            

def random_word(filename):
    words = []
    freqs = []
    total = 0

    novel = process_file(filename)
    for word, freq in novel.items():
        total += freq
        words.append(word)
        freqs.append(total)

    print("random words:")
    for count in range(10):
        index = randint(0, total)
        find = in_disect(index, freqs, 0 , len(freqs) )
        print(words[find], end = ' ')
        

def main():
    random_word('frankenstein_cut.txt')

if __name__ == "__main__":
    main()