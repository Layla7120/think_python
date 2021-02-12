def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]


#like_aways_palindrome
# def is_palindrome(word):
#     end = len(word) - 1
#     for a in range(len(word)//2 + 1):
#         if a >= end:
#             return True
#         if word[a] == word[end]:
#             end -= 1
#         else: 
#             return False
#one-sentence-version
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

#1
print(first("hi"))
print(last("word"))
print(middle("hi"))
print(middle("a"))
print(middle(''))

#2
print(is_palindrome("토마토"))
print(is_palindrome("noon"))
print(is_palindrome("happy"))
print(is_palindrome("redivider"))
print(is_palindrome("moon"))