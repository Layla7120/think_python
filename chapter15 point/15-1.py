import math, copy

class point:
    ''' 2차원 공간에 점을 표현한다'''

class Rectangle:
    ''' 사각형을 표시한다.
    속성: width, height, corner
    '''

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

 #연습
def distance_between_points(p):
    return p.x - p.y

class circle:
    center = point()
    radius = int


def point_in_circle(Circle, Point):
    x_subs = abs(Circle.center.x - Point.x)
    y_subs = abs(Circle.center.y - Point.y)
    if x_subs**2 + y_subs**2 <= Circle.radius ** 2:
        return True
    return False

def rect_in_circle(Circle, Rectangle):
    corner = copy.deepcopy(Rectangle.corner)
    if point_in_circle(Circle, corner):
        corner.x = corner.x + Rectangle.width
        if point_in_circle(Circle, corner):
            corner.y = corner.y - Rectangle.height
            if point_in_circle(Circle, corner):
                corner.x = corner.x - Rectangle.width
                if point_in_circle(Circle, corner):
                    return True
                return ("(0,y) not included")
            return ("(x,y) not included")
        return ("(x,0) not included")
    return ("(0,0) not included")

def rect_circle_overlap(Circle, Rectangle):
    corner = copy.deepcopy(Rectangle.corner)
    if point_in_circle(Circle, corner):
        return True
        corner.x = corner.x + Rectangle.width
        if point_in_circle(Circle, corner):
            return True
            corner.y = corner.y - Rectangle.height
            if point_in_circle(Circle, corner):
                return True
                corner.x = corner.x - Rectangle.width
                if point_in_circle(Circle, corner):
                    return True
    return False
                



def main():
    # blank = point()
    # blank.x = 3.0
    # blank.y = 4.0
    # print(distance_between_points(blank))

    Circle = circle()
    Circle.center.x = 0
    Circle.center.y = 0
    Circle.radius = 150

    dot = point()
    dot.x = 4
    dot.y = 0

    box = Rectangle()
    box.width = 300.0
    box.height = 100.0
    box.corner = point()
    box.corner.x = 160.0
    box.corner.y = 0.0

    print(point_in_circle(Circle, dot))
    print(rect_in_circle(Circle, box))
    print(rect_circle_overlap(Circle, box))

if __name__ == "__main__":
    main()
