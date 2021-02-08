import math
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
        t.lt(angle)


def tri(t, n):
    length = 100
    t.fd(length)
    t.lt(180 - (90 - 180 / n))
    t.fd(2*length * math.sin(math.pi / n))
    t.lt(180 - (90 - 180 / n))
    t.fd(length)


def figure(n):
    angle_fig = 360 / n
    for i in range(n):
        tri(bob, n)
        bob.lt(180)


bob = turtle.Turtle()
figure(5)
figure(6)
figure(7)


# wait for the user to close the window
turtle.mainloop()
