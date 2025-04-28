import math
from math import sqrt

from prettytable import PrettyTable


def Input_Litter(Litter):
    try:
        P = (input(f"Введите координаты {Litter} через пробел -> ").split())
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
    return array_chet[-1]


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

P = Input_Litter("P")
X = Input_Litter("X")
c = int(input("c = "))

if P in array_full:
    X_LKG = [X]
    print(f"1) Линейный конгруэнтный генератор:\n"
          f"X(i+1) = c * X(i) + P = {c} * X(i) + {P}\n"
          f"X(0) = {X}")
    while True:
        num = find_xP(c, X_LKG[-1])
        if num != P:
            x_next = poisk_sum(num, P)
        else:
            x_next = poisk_um(num)
        print(f"X({len(X_LKG)}) = {c} * {X_LKG[-1]} + {P} = {find_xP(c, X_LKG[-1])} + {P} = {x_next}")
        X_LKG.append(x_next)
        if x_next in X_LKG[1:-1]:
            break
    print(f"Период = {len(X_LKG[1:-1])}\n\n")

    X_IG = [X]
    print(f"1) Инверсивный генератор:\n"
          f"X(i+1) = c * X(i)^-1 + P = {c} * X(i)^-1 + {P}\n"
          f"X(0) = {X}")
    while True:
        if X_IG[-1] == 'O':
            X_obr = 'O'
        else:
            X_obr = (X_IG[-1][0], -X_IG[-1][1] % p)
        num = find_xP(c, X_obr)
        if num != P:
            x_next = poisk_sum(num, P)
        else:
            x_next = poisk_um(num)
        print(f"X({len(X_IG)}) = {c} * {X_obr} + {P} = {find_xP(c, X_obr)} + {P} = {x_next}")
        X_IG.append(x_next)
        if x_next in X_IG[1:-1]:
            break
    print(f"Период = {len(X_IG[1:-1])}")
    def Array_str(mass):
        string = ''
        for i in range(len(mass)):
            if len(mass[i]) != 1:
                string += f"({mass[i][0]}, {mass[i][1]}) "
            else:
                string += f"{mass[i]} "
        return string
    print(f"Ответ:\n"
          f"1){Array_str(X_LKG[:-2])}\n"
          f"2){Array_str(X_IG[:-2])}\n")
else:
    print("Это не точка ЭК")