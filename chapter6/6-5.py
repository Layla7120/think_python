def gcd(a,b):
    if b == 0:
        return a
    else: 
        r = a % b
        return gcd(b, r)

print(gcd(10, 3))
print(gcd(16, 32))
print(gcd(42,49))