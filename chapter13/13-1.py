import string

def organize(word_doc):
    wordlist = []
    for line in word_doc:
        word = line.lower().split() 
        for text in word:
            for a in string.punctuation:
                text = text.replace(a ,' ')
            text = text.strip()
            wordlist.append(text)    
    return wordlist

if __name__ == "__main__":
    wordlist = open("frankenstein_cut.txt")
    print(organize(wordlist))
    