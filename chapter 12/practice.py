def sumall(*all):
    total = 0
    for a in all: 
        total += a
    return total

print(sumall(1, 2, 3))