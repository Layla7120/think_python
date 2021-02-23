# def is_anagram(array1, array2):
#     array1 = list(array1)
#     array2 = list(array2)
#     array1.sort()
#     array2.sort()
#     if array1 == array2:
#         return True
#     else:
#         return False

# 코드 직접 짜봤으나 너무 오래 걸려서 해설 참조
# def find_anagram():
#     fin = open('words.txt')

#     anag = dict()
#     line = fin.readlines()
#     for index in range(len(line)):
#         word = line[index].strip()
#         for index2 in range(index + 1,len(line)):
#             word2= line[index2].strip()
#             if is_anagram(word,word2):
#                 if word in anag:
#                     anag[word] += [word2]
#                 else:
#                     anag[word] = [word,word2]
#     for a in anag:
#         print(anag[a])


def signature(s):
    """Sort 해서 정리한 값을 리턴함
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """애너그램을 찾으면 계속 추가하는 함수"""
    d = {}
    for line in open('words.txt'):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """애너그램 세트를 반환하는 함수"""
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)

#2
def print_anagram_sets_in_order(d):
    """그냥 sort 써버리기"""
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)

#3
def filter_length(d, n):
    """Select only the words in d that have n letters.
    d: map from word to list of anagrams
    n: integer number of letters
    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    print_anagram_sets(all_anagrams('words.txt'))
    print_anagram_sets_in_order(all_anagrams('words.txt'))