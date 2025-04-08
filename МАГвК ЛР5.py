from prettytable import PrettyTable


def inference(array, task):
    numbers = [str(i) for i in range(0, len(array_x))]
    table = PrettyTable()
    table.field_names = [""] + [f"{num+1}" for num in range(len(numbers))]
    if task == 'x':
        table.add_row(['x'] + numbers)
        table.add_row([f"x^3 + {a}x + {b} (mod {p})"] + array)
    elif task == 'y':
        table.add_row(["y"] + numbers)
        table.add_row([f"    y^2 (mod {p})     "] + array)
    table.header = False
    for i in table.field_names:
        table.align[i] = "c"
    return table


def poisk_sum(P, Q):
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

P = (0, 0)
try:
    P = (input("Введите координаты P через пробел -> ").split())
except:
    print("Введено не правильно")

count = int(input("Какое P посчитать ->")) + 1
array_chet = [(0, 0)]
while len(array_chet) != count:
    if len(array_chet) == 1:
        array_chet.append(P)
        continue
    elif len(array_chet) != 1 and len(array_chet) % 2 == 0:
        array_chet.append(poisk_um(array_chet[len(array_chet) // 2]))
    else:
        array_chet.append(poisk_sum(array_chet[1], array_chet[-1]))

for i in range(1, len(array_chet)):
    if len(array_chet[i]) == 2:
        print(f"{' '*(2-len(str(i)))}{i}P = ({array_chet[i][0]},{array_chet[i][1]})")
    else:
        print(f"{' ' * (2 - len(str(i)))}{i}P = {array_chet[i]}")

