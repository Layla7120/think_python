import operator

def most_frequent(text):
    freq = dict()
    print(text)
    for a in text:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    new_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    return new_freq

if __name__ == '__main__':
    print(most_frequent("hello"))
    novel = open('frankenstein_cut.txt').read()
    print(most_frequent(novel))

