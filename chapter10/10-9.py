import time
fin = open('words.txt')
start = time.time()
t = []
for line in fin:
    word = line.strip()
    t.append(word)
        
end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start))
start = time.time()
t = []
for line in fin:
    word = line.strip()
    t = t + [word]

print("WorkingTime: {} sec".format(time.time()-start))
