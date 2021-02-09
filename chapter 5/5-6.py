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

def koch(t, x):
    '''
    t.fd(x/3)
    t.lt(60)
    t.fd(x/3)
    t.rt(120)
    t.fd(x/3)
    t.lt(60)
    t.fd(x/3)

    t.fd(x/3)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    '''
    

def snowflake(t, x):
    polyline(t, 3, x, 60)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)

turtle.mainloop()




bob = turtle.Turtle()
koch(bob, 300)

turtle.mainloop()