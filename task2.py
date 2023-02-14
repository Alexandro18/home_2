#Даны три натуральных числа A, B, C. Определите, существует ли треугольник с такими сторонами

if __name__ == '__main__':
    A, B, C = int(input()), int(input()), int(input())

    if A + B > C or A + C > B or C + B > A:
        print('YES')
    else:
        print('NO')