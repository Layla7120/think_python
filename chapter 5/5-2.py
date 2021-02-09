def check_ferma(a, b, c, n):
    n = int(n)
    if n > 2 and type(n) == int:
        if int(c) == int(a) ** n + int(b) ** n:
            return False
    else:
        return "out of range"
    return True

a, b, c, n = input('a, b, c, n: ').split(",")
print(check_ferma(a, b, c, n))