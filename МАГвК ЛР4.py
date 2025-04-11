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


def Equation(function, x):
    return eval(function.replace('x', str(x)))


a = int(input('Введите a -> '))
b = int(input('Введите b -> '))
p = int(input('Введите p -> '))
function = f"x**3+{a}*x+{b}"
print(f"Необходимо найти все точки ЭК:\n\t y^2 = x^3 + {a}x + {b} (mod {p})")

array_x, array_y = [], []
for i in range(p):
    array_x.append(Equation(function, i) % p)
    array_y.append((i*i) % p)

print(inference(array_x, 'x'))
print(inference(array_y, 'y'))

array_per = ["O"]
for x in range(len(array_x)):
    if array_x[x] in array_y:
        for y in range(len(array_y)):
            if array_x[x] == array_y[y]:
                array_per.append(f"{x}, {y}")
print('(' + ');('.join(array_per[1:]) + ')' + f" и {array_per[0]}")
print(f"   ПЭК = {len(array_per)}\n")

P = (0, 0)
Q = (0, 0)
try:
    P = (input("Введите координаты P через пробел -> ").split())
    Q = (input("Введите координаты Q через пробел -> ").split())
except:
    print("Введено не правильно")

if len(P) == 2 and len(Q) == 2:
    P = (int(P[0]), int(P[1]))
    Q = (int(Q[0]), int(Q[1]))
    if P[0] != Q[0]:
        cheak = 0
        for i in range(1, len(array_per)):
            sim1, sim2 = array_per[i].split(", ")
            if P[0] == int(sim1) and P[1] == int(sim2):
                cheak += 1
            if Q[0] == int(sim1) and Q[1] == int(sim2):
                cheak += 1

        if cheak == 2:
            k_sum = pow((Q[1] - P[1]) * pow((Q[0] - P[0]), -1, p), 1, p)
            x3 = (k_sum**2 - P[0] - Q[0]) % p
            y3 = (k_sum * (P[0] - x3) - P[1]) % p

            k_mult = pow((3 * P[0] ** 2 + a) * pow((2 * P[1]), -1, p), 1, p)
            x4 = (k_mult**2 - 2 * P[0]) % p
            y4 = (k_mult * (P[0] - x4) - P[1]) % p
            print(f'P{P}\n'
                  f'Q{Q}\n'
                  f'\tP+Q:\n'
                  f'λ = {k_sum}\n'
                  f'Точка ({x3}, {y3})\n'
                  f'\t2P:\n'
                  f'λ = {k_mult}\n'
                  f'Точка ({x4}, {y4})')
        else:
            print(f"Точки не принадлежит прямой")
    else:
        print('Бесконечно удаленная')
else:
    print("Координаты введены не правильно")