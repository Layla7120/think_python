import string

#몇줄 이상 되어야 제대로 돌아감
def organize(word_doc):
    '''
    각 줄에 있는 단어를 공백 단위로 자르고 기호는 없애줌
    '''
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
    
    # print("total words:" + str(total) + " \n most used:" + str(new_count[0]))
    # print(type(new_count))
    return new_count

def not_in_list(listofwords):
    t = []
    wordlist = open("words.txt").read()
    for a in listofwords:
        if a not in wordlist:
            t.append(a)
    print(t)

if __name__ == "__main__":
    wordlist = open('frankenstein_cut.txt', 'rt', encoding='UTF8')
    not_in_list(organize(wordlist))
    