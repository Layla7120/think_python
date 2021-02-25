import math, copy
import turtle

class point:
    ''' 2차원 공간에 점을 표현한다'''

class Rectangle:
    ''' 사각형을 표시한다.
    속성: width, height, corner
    '''

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


class circle:
    center = point()
    radius = int

def draw_rectangle(t, Rectangle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(2):
        t.fd(Rectangle.width)
        t.lt(90)
        t.fd(Rectangle.height)
        t.lt(90)

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


def draw_circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def main():
    # blank = point()
    # blank.x = 3.0
    # blank.y = 4.0
    # print(distance_between_points(blank))

    Circle = circle()
    Circle.center.x = 0
    Circle.center.y = 0
    Circle.radius = 150

    box = Rectangle()
    box.width = 300.0
    box.height = 100.0
    box.corner = point()
    box.corner.x = 160.0
    box.corner.y = 0.0

    bob = turtle.Turtle()
    # draw_rectangle(bob, box)
    draw_circle(bob, Circle.radius)



if __name__ == "__main__":
    main()

    turtle.mainloop()
