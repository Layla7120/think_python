def subtract(d1, d2):
    return set(d1) - set(d2)

import string

def process_file(filename):
    hist = dict()
    fp = open(filename, encoding= 'utf-8')
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-',' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def main():
    hist =process_file('emma.txt')
    words = process_file('words.txt')
    diff = subtract(hist, words)
    print("Words in the book that aren't in the word list:")

    for word in diff:
        print(word, end = ' ')

if __name__ == "__main__":
    main()