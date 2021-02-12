def rotate_word(word, code):
    new_word = ""
    temp = ""
    for a in word:
        temp = ord(a)
        # print(temp, chr(temp))
        if temp > 64 and temp < 91:
            temp = temp - 65
            count = temp + code
            if count < 0:
                count = 26 + count
            temp = count + 65
            #print(count,"high", temp)
        elif temp > 96 and temp < 123:
            temp = temp - 97
            count = temp + code
            if count < 0:
                count = 26 + count
            temp = count + 97
            # print(count,"low", temp)
        else:
            return "not alphabet" 
        new_word = new_word + chr(temp)
    return new_word



print(rotate_word("cheer", 7))
print(rotate_word("melon", -10))
print(rotate_word("HAL", 1))

