def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def mile_palindrome(miles):
    str_miles = str(miles)
    last = len(str_miles)
    if last == 6:
        if is_palindrome(str_miles[last - 4: last]):
            miles += 1
            str_miles = str(miles)
            if is_palindrome(str_miles[last - 5: last]):
                miles += 1
                str_miles = str(miles)
                if is_palindrome(str_miles[last - 5: last-1]):
                    miles += 1
                    str_miles = str(miles)
                    if is_palindrome(str_miles):
                        return True

num = 0
while num < 1000000:
    if mile_palindrome(num): 
        print(num)
        break
    num += 1
