def is_anagram(array1, array2):
    array1 = list(array1)
    array2 = list(array2)
    array1.sort()
    array2.sort()
    if array1 == array2:
        return True
    else:
        return False

def find_anagram():
    fin = open('test.txt')
    anag = dict()
    line = fin.readlines()
    for index in range(len(line)):
        word = line[index].strip()
        print(index, len(line))
        for index2 in range(index + 1,len(line)):
            print(index2, len(line))
            word2= line[index2].strip()
            if is_anagram(word,word2):
                if word in anag:
                    anag[word].append(word2)
                else:
                    anag[word].append(word, word2)
    return anag


if __name__ == '__main__':
    print(find_anagram())
