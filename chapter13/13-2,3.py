import string

def organize(word_doc):
    wordlist = []
    for line in word_doc:
        word = line.lower().split() 
        for text in word:
            for a in string.punctuation:
                text = text.replace(a ,'')
            text = text.strip()
            wordlist.append(text)    
    return wordlist

import operator

def count_word(wordlist):
    count = {}
    total = 0
    for a in wordlist:
        total += 1
        if a in count:
            count[a] += 1
        else:
            count[a] = 0
    new_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    
    print("total words:" + str(total) + " \n most used:" + str(new_count[0]))
    return new_count

def print_most_twenty(word_dict):
    for a in range(10):
        print(word_dict[a])

if __name__ == "__main__":
    wordlist = open('emma.txt', 'rt', encoding='UTF8')
    print_most_twenty(count_word(organize(wordlist)))
    