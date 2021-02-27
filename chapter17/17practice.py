# class Time:
#     '''시간을 표현  
#     속성: hour, minute, second
#     '''
#     def __str__(self):
#         return '%.2d:%2d:%2d' %(self.hour, self.minute, self.second)

# def print_time(t):
#     """Prints a string representation of the time.
#     t: Time object
#     """
#     print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

# def main():
#     noon_time = Time()
#     noon_time.hour = 9
#     noon_time.minute = 0
#     noon_time.second = 0
#     print(noon_time)


# if __name__ == "__main__":
#     main()



class point:
    ''' 2차원 공간에 점을 표현한다'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d, %d)' %(self.x, self.y)
    
    def __add__(self, other):
        if isinstance(other, point):
            self.x += other.x
            self.y += other.y
            return self
        else:
            point_1 = point()
            point_1.x = other[0]
            point_1.y = other[1]
            return point_1

def main():
    noon_time = point(9, 0)
    other_time = point(10, 30)
    print(noon_time + other_time)


if __name__ == "__main__":
    main()