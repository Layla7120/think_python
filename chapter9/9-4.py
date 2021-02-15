fin = open('words.txt')

def uses_only(a, words):
    count = 0
    for letter in a:
        if letter in words:
            count += 1
    if count == 1:
        return True
    else:
        return False

def counting(must):
    for line in fin:
        if uses_only(line, must):
            print(line)
    

must = input("포함할 단어: ")
counting(must)
# print(uses_only("hello", "h"))


















