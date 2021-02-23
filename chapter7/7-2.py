import math

def eval_loop():
    result = "done"
    while True:
        word = input()
        if word == "done":
            break
        result = eval(word)
        print(result)
    return result

print(eval_loop())