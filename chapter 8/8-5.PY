# def rotate_word(word, code):
#     new_word = ""
#     temp = ""
#     for a in word:
#         temp = ord(a)
#         # print(temp, chr(temp))
#         if temp > 64 and temp < 91:
#             temp = temp - 65
#             count = temp + code
#             if count < 0:
#                 count = 26 + count
#             temp = count + 65
#             #print(count,"high", temp)
#         elif temp > 96 and temp < 123:
#             temp = temp - 97
#             count = temp + code
#             if count < 0:
#                 count = 26 + count
#             temp = count + 97
#             # print(count,"low", temp)
#         else:
#             return "not alphabet" 
#         new_word = new_word + chr(temp)
#     return new_word



print(rotate_word("cheer", 7))
print(rotate_word("melon", -10))
print(rotate_word("HAL", 1))

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))