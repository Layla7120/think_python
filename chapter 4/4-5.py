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


def spiral(t, angle):
    """Draws an arc with the given radius and angle.
        t: Turtle
        r: radius
        angle: angle subtended by the arc, in degrees
        """
    for i in range(angle):
        r = 200 * math.radians(i)
        arc_length = 2 * math.pi * r * abs(angle) / 360
        n = int(arc_length / 2) + 3
        step_length = arc_length / n
        step_angle = float(angle % 360) / n
        # making a slight left turn before starting reduces
        # the error caused by the linear approximation of the arc
        polyline(t, i, step_length, step_angle)


bob = turtle.Turtle()

spiral(bob, 90)



# wait for the user to close the window
turtle.mainloop()
