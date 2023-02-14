# Задача для отважных
# Есть две коробки, первая размером A1×B1×C1, вторая размером A2×B2×C2.
# Определите, можно ли разместить одну из этих коробок внутри другой,
# при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

if __name__ == '__main__':

    A1, B1, C1 = int(input()), int(input()), int(input())
    A2, B2, C2 = int(input()), int(input()), int(input())

    if (A1 == A2 and B1 == B2 and C1 == C2) or (A1 == A2 and C1 == B2 and B1 == C2) or (B1 == A2 and A1 == C2 and C1 == B2) or (B1 == A2 and C1 == C2 and A1 == B2) or (C1 == A2 and A1 == C2 and B1 == B2) or (C1 == A2 and B1 == C2 and A1 == B2):
        print('Boxes are equal')
    elif A1 * B1 * C1 > A2 * B2 * C2:
        print('The first box is larger than the second one')
    else:
        print('The second box is larger than the first one')