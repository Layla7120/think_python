fin = open('words.txt')

def has_no_e(word):
    for a in word:
        if a == 'e':
            return False
        else:
            return True

count = 0
total = 0
for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
    total += 1

print(count / total * 100)
