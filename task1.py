# нужно выяснить можешь ли сбить пешка фигуру

if __name__ == '__main__':

    a1, b1, a2, b2 =  int(input()), int(input()), int(input()), int(input())

    if a2 - a1 == 1 and (b2 - b1 == -1 or b2 - b1 == 1):
        print('YES')
    else:
        print("NO")
