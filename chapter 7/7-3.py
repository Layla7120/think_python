import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

def estimate_pi():
    k = 0
    sum = 0
    while True:
        result = (factorial(4*k) * (1103 + 26390 * k)) / ((factorial(k)**4) * 396 ** (4*k))
        sum += result
        if result <= 1e-15:
            break
        k += 1
    est = 1 / ((2 * math.sqrt(2) / 9801) * sum)
    
    return est



print(factorial(4))
print(estimate_pi())