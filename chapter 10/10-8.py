from random import randint
for a in range(1000):
    count = 0
    student = []
    for a in range(1, 24):
        student = student + [randint(1, 100)]
        # print(a, n)

    for a in range(1, 24):
        for b in range(a + 1, 23):
            if student[a] == student[b]:
                count += 1
print(count)
