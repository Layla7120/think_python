import math

def display(img):
    column, row= len(img), len(img[0])
    for i in range(column):
        for j in range(row):
            print(img[i][j], end=' ')
        print()

def mysqrt(a):
    epsilon = 0.0000001
    x = 1.0
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    column, row = 4, 11
    #chart format
    array = [[0 for _ in range(column)] for _ in range(row)]
    array[0][0] = "a  "
    array[0][1] = "mysqrt(a)"
    array[0][2] = "math.sqrt(a)"
    array[0][3] = "diff"
    array[1][0] = "-  "



    array[1][1] = "---------     "
    array[1][2] = "------------"
    array[1][3] = "----"

    #chart insert
    for count in range(2, row):
        a = float(count-1)
        array[count][0] = a
        array[count][1] = round(mysqrt(a),11)
        array[count][2] = round(math.sqrt(a), 11)
        array[count][3] = round(round(mysqrt(a),11) - round(math.sqrt(a), 11), 11)
    return array

array_img = test_square_root()






display(array_img)


