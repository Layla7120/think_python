def is_triangle(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    a, b = swap(a, b)
    a, c = swap(a, c)
    b, c = swap(b, c)
    if c >= a + b:
        return False
    else:
        return True

def swap(a, b):
    if a > b:
        temp = a
        a = b 
        b= temp
    return a, b
    
a, b, c = input('a,b,c:').split(",")
print(is_triangle(a, b, c))
