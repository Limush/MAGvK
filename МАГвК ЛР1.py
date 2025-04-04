import random


def Nod(a, b, count=0):
    while True:
        count += 1
        a, b = b, a % b
        if b == 0:
            return a


def find_S_t(n, count=1):
    degrees_2 = []
    while True:
        if count > n:
            break
        degrees_2.append(count)
        count *= 2

    for num in range(len(degrees_2) - 1, -1, -1):
        if (n - 1) % degrees_2[num] == 0 and ((n - 1) // degrees_2[num]) % 2 == 1:
            return num, (n - 1) // degrees_2[num]


# number = 1323
# number = 99733
# number = 99751
number = 99881

b = 0
if number >= 3:
    print(f"Проверить являеться ли число n={number} простым:")
    # Пункт 1 - поиск S и t:
    print(f"\t\t\tПункт 1:\nПоиск S и t по формуле n-1=2**s*t:")
    S, t = find_S_t(number)
    if S > 0:
        print(f"\t{number - 1} = 2**{S} * {t}")
        spisok_a, count = [], 0
        a_mass = random.sample(range(2, number-1), number-3)

        while len(spisok_a) != 5:
            if count >= len(a_mass):
                break
            elif Nod(a_mass[count], number) == 1:
                spisok_a.append(a_mass[count])
            count += 1

        string = ''
        for i in range(S):
            if i != S-1:
                string += str(i) + ';'
            else:
                string += str(i)

        for i in range(len(spisok_a)):
            print(f"\t\t\tПункт {i+1}.2\n"
                  f"Пусть a = {spisok_a[i]} 2<={spisok_a[i]}<={number-2}, k=0 (k<S, S={S}, k={string})\n"
                  f"\t\t\tПункт {i+1}.3\n"
                  f"НОД({number};{spisok_a[i]}) = 1")
            for y in range(S):
                if y == 0:
                    b = spisok_a[i]**t % number
                save_b = b
                print(f"\t\t\tПункт {i+1}.4\n"
                      f"b = {spisok_a[i]}**{t}(mod{number}) = {b}(mod{number})")
                if b == 1 or b == number - 1:
                    print(f"\tЧисло {number} вероятно простое\n\n\n")
                    break
                b = b**2 % number

                print(f"\t\t\tПункт {i + 1}.5\n"
                      f"Так как {save_b} != 1 и {save_b} != {number-1}, то b=b**2(mod{number})\n"
                      f"-> b = {save_b}**2(mod{number}) = {b}(mod{number})")

                if b == number - 1:
                    print(f"\t\t\tПункт {i+1}.6\n"
                          f"b = n - 1 = {b}\nЧисло {number} вероятно простое\n\n\n")
                    break
            else:
                print(f"{b} != {number-1} и k={S-1}, то алгоритм закончен\n"
                      f"Число {number} составное\n"
                      f"\t\t\tИтог:\nЧисло {number} составное")
                break
        else:
            print(f"\t\t\tИтог:\nПо итогу 5 проверок сделаем вывод что число {number} - вероятно просто")
    else:
        print(f"Число {number} составное")