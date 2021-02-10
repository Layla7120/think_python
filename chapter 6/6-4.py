def is_power(a, b):
    if a % b == 0:
        if a / b % b == 0:
            return True
    return False


print(is_power(9,3))
print(is_power(16,4))
print(is_power(25,3))