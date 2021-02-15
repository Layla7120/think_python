fin = open('words.txt')

def avoids(word, avoid_words):
    for letter in word:
        if letter in avoid_words:
            return False
    return True

def counting(avoid):
    count = 0
    for line in fin:
        if avoids(line, avoid):
            count += 1
    return count


avoid = input("금지할 단어")
print(counting(avoid))
# print(avoids("hello", "ol"))    