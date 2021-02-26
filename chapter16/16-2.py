from datetime import datetime, date
import copy
now = datetime.now()
now_date = date.today()

def print_time(t):
    """Prints a string representation of the time.
    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.year, t.month, t.day))

def next_birthday(Date):
    age = now.year - Date.year
    birthday = date(Date.year + age, Date.month, Date.day)
    # print_time(birthday)
    # print_time(now_date)
    if birthday == now_date:
        'Happy Birthday'
    elif birthday < now_date:
        next = datetime(birthday.year + 1, Date.month, Date.day + 1, 0, 0, 0)
        date_diff = next - now
        print('passed' + str(date_diff))
    else:
        birthday = datetime(birthday.year, Date.month, Date.day + 1, 0, 0, 0)
        date_diff = birthday - now
        print('until next birthday: '+ str(date_diff))
    # datetime.timedelta
    

def double_day(people1, people2):
    age_gap = abs(people1.year - people2.year)
    if people1 == people2:
        return 'are you joking?'
    elif people1 < people2:
        younger = people2
        elder = people1
    else:
        younger = people1
        elder = people2
    
    
    #생일 달,월 비교
    compare = datetime(elder.year + age_gap, elder.month, elder.day,0,0,0)
    if compare == younger:
        return "NO WAY"
    elif compare > younger:
        # print(compare, elder)
        return date(younger.year + age_gap, elder.month, elder.day)
    else:
        # print(compare, elder)
        return date(younger.year + age_gap, younger.month, younger.day )

    

def mutiple_day(people1, people2, n):
    age_gap = abs(people1.year - people2.year)
    key_age = age_gap / (n - 1)
    if age_gap % (n - 1) != 0 or key_age <= 1:
        return "Can't find exact date."

    if people1 == people2:
        return 'are you joking?'
    elif people1 < people2:
        younger = people2
        elder = people1
    else:
        younger = people1
        elder = people2
    

    #생일 달,월 비교
    compare = datetime(elder.year + age_gap, elder.month, elder.day,0,0,0)
    if compare == elder:
        return "NO WAY"
    elif compare > younger:
        return date(younger.year + int(key_age), elder.month, elder.day)
    else:
        return date(younger.year + int(key_age), younger.month, younger.day)

    

def main():
    # birth_date = input("YYYY-MM-DD: ")
    # # birth_date = '1999-07-12'
    # birth = date.fromisoformat(birth_date)
    
    # next_birthday(birth)

    b1 = datetime(2011, 10, 11)
    b2 = datetime(2003, 12, 26)
    print('Double Day:', end=' ')
    print(double_day(b1, b2))
    n = 5
    print('mutiple_day',n,"times older:", end=' ')
    print(mutiple_day(b1, b2, n))


if __name__ == "__main__":
    main()