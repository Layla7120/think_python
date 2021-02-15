fin = open('words.txt')

def uses_all(a, words):
    count = 0
    for letter in a:
        if letter in words:
            count += 1
    if count >= 1:
        return True
    else:
        return False

def counting(avoid):
    count = 0
    for line in fin:
        if uses_all(line, avoid):
            count += 1
    return count
    

must = input("포함할 단어: ")
print(counting(must))
# print(uses_only("hello", "h"))

