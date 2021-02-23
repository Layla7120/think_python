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


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)


def flower(n):
    for i in range(n):
        bob.pd()
        arc(bob, 100, 2 * 180 / n)
        bob.pu()
        bob.lt(180 - 2 * 180 / n)
        bob.pd()
        arc(bob, 100, 2 * 180 / n)
        bob.pu()
        bob.lt(180)
        bob.pd()


def flower_mod(n):
    for i in range(n):
        bob.pd()
        arc(bob, 100, 2 * 360 / n)
        bob.pu()
        bob.lt(180 - 2 * 360 / n)
        bob.pd()
        arc(bob, 100, 2 * 360 / n)
        bob.pu()
        bob.lt((360/n)*(n/2 - 1))
        bob.pd()


bob = turtle.Turtle()

# flower(7)
# flower(20)
flower_mod(9)


# wait for the user to close the window
turtle.mainloop()
