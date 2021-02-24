from __future__ import print_function, division
import anagram_sets
import sys, shelve


def store_anagrams(filename, anagram):
    shelf = shelve.open(filename, 'c')

    for key, index in anagram.items():
        shelf[key] = index

    shelf.close()

    
def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sig = anagram_sets.signature(word) #정렬해야 리스크 불러올 수 있음
    print(word)
    try: 
        return shelf[sig]

    except KeyError:
        return []


def main(script, command = 'make_db'):
    print(command)
    if command == 'make_db':
        anagram_map = anagram_sets.all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))

if __name__ == '__main__':
    main(*sys.argv)
    main('wendigos')
    
