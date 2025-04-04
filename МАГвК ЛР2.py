def Nod(a, b):
    if a == 0 or b == 0:
        return 0
    while True:
        a, b = b, a % b
        if b == 0:
            return a


def funk(x):
    return eval(function.replace('x', str(x))) % n


n = int(input('Число n = '))
c, function = int(input('Число c = ')), input("Введите функцию -> ")

a, b, num = 1, 1, 0
while True:
    print(f'i = {num + 1}:')
    if num == 0:
        a, b = funk(c), funk(funk(c))
        print(f'\ta = f({c}) = {a}\n\tb = f(f({c})) = {b}')
    else:
        a_save, b_save = a, b
        a, b = funk(a), funk(funk(b))
        print(f'\ta = f({a_save}) = {a}\n\tb = f(f({b_save})) = {b}')
    num += 1

    d = Nod((a - b) if a > b else (b - a), n)
    if d > 1:
        print(f'\td = НОД({(a - b) if a > b else (b - a)},{n}) = {d} - нетривиальный делитель числа {n}')
        print(f'Ответ: {n} = {d} * {n // d}')
        break
    elif d == 1:
        print(f'\td = НОД({(a - b) if a > b else (b - a)},{n}) = {d}\n')
    else:
        print(f'a = {a}; b = {b} - неподвижная точна\n⇒ делитель не найден\n\n')
        function = input("Введите новую функцию -> ")
        num = 0
    if num == 100:
        print(f'За 100 итерация не было найдено делителя числа {n}')
        break
