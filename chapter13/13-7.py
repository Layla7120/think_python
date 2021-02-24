def cumsum(t):
    total = 0
    for a in range(len(t)):
        total += t[a]
        t[a] = total
    return t

def process_file(filename):
    hist = dict()
    fp = open(filename, encoding= 'utf-8')
    for line in fp:
        process_line(line, hist)
    return hist

import string

def process_line(line, hist):
    line - line.replave('-', ' ')

    for word in line:
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def word_total():
    
def main():
