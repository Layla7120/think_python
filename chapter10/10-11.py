def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def reverse_pair(t1, t2):
    test = t1 + t2
    # print(test)
    if is_palindrome(test):
        return True
    return False

print(reverse_pair("apple", "elppa"))
print(reverse_pair("pencil", "licenp"))