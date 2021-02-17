def is_anagram(array1, array2):
    array1 = list(array1)
    array2 = list(array2)
    array1.sort()
    array2.sort()
    if array1 == array2:
        return True
    else:
        return False

print(is_anagram("word", "dowr"))
print(is_anagram("halsey", "ashley"))