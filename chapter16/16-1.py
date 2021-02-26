class Time:
    '''시간을 표현  
    속성: hour, minute, second
    '''

def mul_time(Time, number):
    int_time = time_to_int(Time)
    int_time = int_time * number
    return int_to_time(int_time)

def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def print_time(t):
    """Prints a string representation of the time.
    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def miles_per_hour(Time, miles):
    time = time_to_int(Time)
    mph = time / miles 
    mph = int_to_time(mph)
    return mph

def main():
    noon_time = Time()
    noon_time.hour = 9
    noon_time.minute = 0
    noon_time.second = 0


    new_time = mul_time(noon_time, 5)
    print_time(new_time)
    mph = miles_per_hour(new_time, 7)
    print_time(mph)

if __name__ == "__main__":
    main()


