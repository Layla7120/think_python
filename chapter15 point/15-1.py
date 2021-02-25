class point:
    ''' 2차원 공간에 점을 표현한다'''

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

 #연습
def distance_between_points(p):
    return p.x - p.y

class circle:
    center = point()
    radius = int

import math

def point_in_circle(Circle, Point):
    x_subs = abs(Circle.center.x - Point.x)
    y_subs = abs(Circle.center.y - Point.y)
    if x_subs**2 + y_subs**2 <= Circle.radius ** 2:
        return True
    return False


if __name__ == "__main__":
    # blank = point()
    # blank.x = 3.0
    # blank.y = 4.0
    # print(distance_between_points(blank))

    circle = circle()
    circle.center.x = 0
    circle.center.y = 0
    circle.radius = 3

    dot = point()
    dot.x = 4
    dot.y = 0

    print(point_in_circle(circle, dot))
