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


a = int(input('Введите a -> '))
b = int(input('Введите b -> '))
p = int(input('Введите p -> '))
function = f"x**3+{a}*x+{b}"

array_x, array_y = [], []
for i in range(p):
    array_x.append(Equation(function, i) % p)
    array_y.append((i*i) % p)

array_per = ["O"]
for x in range(len(array_x)):
    if array_x[x] in array_y:
        for y in range(len(array_y)):
            if array_x[x] == array_y[y]:
                array_per.append(f"{x}, {y}")
print(f"y^2 = x^3 + {a}x + {b} (mod {p})\n"
      f"\tТочки ЭК:")
print('(' + ');('.join(array_per[1:]) + ')' + f" и {array_per[0]}")

P = (10, 8)
try:
    P = (input("Введите координаты P через пробел -> ").split())
    P = (int(P[0]), int(P[1]))
except:
    print("Введено не правильно")

count = 7
while True:
    task = input(f"1 - Поменять точку\n2 - Поменять какое P найти\n3 - Считать для текущих данных\n--->")
    if task == '1':
        try:
            P = (input("Введите координаты P через пробел -> ").split())
            P = (int(P[0]), int(P[1]))
        except:
            print("Введено не правильно")
    elif task == '2':
        count = int(input("Какое P посчитать ->"))
    else:
        cheak = 0
        for i in range(1, len(array_per)):
            sim1, sim2 = array_per[i].split(", ")
            if P[0] == int(sim1) and P[1] == int(sim2):
                cheak += 1

        if cheak == 1:
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
            for i in range(1, len(array_chet)):
                if len(array_chet[i]) == 2:
                    print(f"{' ' * (2 - len(str(i)))}{i}P = ({array_chet[i][0]},{array_chet[i][1]})")
                else:
                    print(f"{' ' * (2 - len(str(i)))}{i}P = {array_chet[i]}")
        else:
            print("Это не точка ЭК")