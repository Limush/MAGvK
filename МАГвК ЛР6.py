import math
from math import sqrt

from prettytable import PrettyTable


def Input_P():
    try:
        P = (input("Введите координаты P через пробел -> ").split())
        P = (int(P[0]), int(P[1]))
        return P
    except:
        print(f"Введено не правильно")
        return False


def poisk_sum(P, Q):
    if P == 'O' and Q != 'O':
        return Q[0], Q[1]
    elif P != 'O' and Q == 'O':
        return P[0], P[1]
    try:
        k_sum = pow((Q[1] - P[1]) * pow((Q[0] - P[0]), -1, p), 1, p)
    except:
        return 'O'
    x3 = (k_sum ** 2 - P[0] - Q[0]) % p
    y3 = (k_sum * (P[0] - x3) - P[1]) % p
    return x3, y3


def poisk_um(P):
    try:
        k_mult = pow((3 * P[0] ** 2 + a) * pow((2 * P[1]), -1, p), 1, p)
    except:
        return 'O'
    x4 = (k_mult ** 2 - 2 * P[0]) % p
    y4 = (k_mult * (P[0] - x4) - P[1]) % p
    return x4, y4


def Equation(function, x):
    return eval(function.replace('x', str(x)))


def find_xP(count, P):
    array_chet = [(0, 0)]
    while len(array_chet) != count + 1:
        if len(array_chet) == 1:
            array_chet.append(P)
            continue
        elif len(array_chet) != 1 and len(array_chet) % 2 == 0:
            array_chet.append(poisk_um(array_chet[len(array_chet) // 2]))
        else:
            num = 1
            while True:
                ob = len(array_chet) - num
                koor = poisk_sum(array_chet[num], array_chet[ob])
                if koor == 'O':
                    num += 1
                else:
                    array_chet.append(koor)
                    break
                if num == len(array_chet):
                    array_chet.append('O')
                    break
    return array_chet


a = int(input('Введите a -> '))
b = int(input('Введите b -> '))
p = int(input('Введите p -> '))
function = f"x**3+{a}*x+{b}"

array_x, array_y = [], []
for i in range(p):
    array_x.append(Equation(function, i) % p)
    array_y.append((i * i) % p)

array_per, array_full = ["O"], ["O"]
for x in range(len(array_x)):
    if array_x[x] in array_y:
        for y in range(len(array_y)):
            if array_x[x] == array_y[y]:
                array_per.append(f"{x}, {y}")
                array_full.append((x, y))
print(f"y^2 = x^3 + {a}x + {b} (mod {p})\n\tТочки ЭК:")
print('(' + ');('.join(array_per[1:]) + ')' + f" и {array_per[0]}")

P = Input_P()
while True:
    task = input(f"1 - Поменять точку\n2 - Считать для текущих данных\n--->")
    if task == '1' or P == False:
        P = Input_P()
    elif task == '2':
        print(array_full)
        print(P)
        if P in array_full:
            print(f"\tПункт 1:")
            N1 = p + 1 + 2 * sqrt(p)
            m = math.ceil(sqrt(N1))
            print(f"N1 = {N1}\n"
                  f"m = {m}")
            print(f"\tПункт 2:")
            P_t = find_xP(m, P)[1:]
            table = PrettyTable()
            table.add_row(['t'] + [i for i in range(1, m + 1)])
            table.add_row(['P(t)'] + P_t)
            table.header = False
            print(table)
            print(f"\tПункт 3:")
            Q = (P_t[-1][0], (P_t[-1][1] * (-1)) % p) if P_t[-1] != 'O' else 'O'
            print(f"Q = {Q}")
            print(f"\tПункт 4:")
            R = 'O'
            print(f"R = {R}")
            print(f"\tПункт 5:")
            t, i = -1, 0
            for y in range(m):
                if R in P_t:
                    t = P_t.index(R)
                    i = y
                    print(f"i = {y}: R = {R} - содержится в табл, при t = {t + 1}")
                    break
                else:
                    print(f"i = {y}: R = {R} - не содержится в табл")
                    if y == 0:
                        R = Q
                    else:
                        R = poisk_sum(P, Q)
                    print(f"=> R = R + Q = {R}")
            if t != -1:
                n = m * i + t + 1
                print(f"=> n = {m} * {i} + {t + 1} = {n}")
                print(f"\tПункт 6:")
                print(f"n = {n}\n")
            else:
                print(f"t не найдено\n")
        else:
            print("Это не точка ЭК")
    else:
        break
