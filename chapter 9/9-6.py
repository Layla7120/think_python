fin = open('words.txt')

def is_abecedarian(word):
    for a in range(len(word) - 1):
        if word[a] > word[a + 1]:
            return False
    return True

def counting():
    count = 0
    for line in fin:
        word = line.strip() # 공백을 지우지 않아서 오류가 계속 생김
        if is_abecedarian(word):
            count += 1
    return count

print(counting())
# print(is_abecedarian("aahed"))