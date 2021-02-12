def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s: 
        falg = c.islower()
    return falg

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase1("helLo"))
print(any_lowercase2("helLO"))
print(any_lowercase3("helLO"))
print(any_lowercase4("helLo"))
print(any_lowercase5("helLo"))