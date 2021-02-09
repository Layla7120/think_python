import turtle
def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def koch(t, x, n):
    if n == 1:
        t.fd(x)
        t.lt(60)
        t.fd(x)
        t.rt(120)
        t.fd(x)
        t.lt(60)
        t.fd(x)
        return
    koch(t, x/3, n - 1)
    t.lt(60)
    koch(t, x/3, n - 1)
    t.rt(120)
    koch(t, x/3, n - 1)
    t.lt(60)
    koch(t, x/3, n - 1)

    

def snowflake(t, x, n):
    koch(t, x/3, n)
    t.rt(120)
    print("in")
    koch(t, x/3, n)
    t.rt(120)
    koch(t, x/3, n)
    t.rt(120)


bob = turtle.Turtle()
#koch(bob, 200, 4)
snowflake(bob, 200 , 3)

turtle.mainloop()