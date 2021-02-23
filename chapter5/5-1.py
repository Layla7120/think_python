import time
time = time.time()
days = ((time // 3600) // 24)
day = (time // 60 // 60 // 24) % 365
hour = (time // 60 // 60) % 12 - 3
min = (time // 60) % 60
sec = time % 60
print("hour =", hour, "min =", min, "sec = ",sec)
print("days after 1970-01-01:", days)