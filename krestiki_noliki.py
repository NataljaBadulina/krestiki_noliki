
# Приветствие
def start():
    print("_____________________")
    print(" Крестики-нолики  3х3")
    print("_____________________")

# Рисуем таблицу


def show_field():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        print(f"  {i} | {' | '.join(row)} | ")
        print("  --------------- ")
    print()

# Проверка вводимых значениЙ


def ask():
    while True:
        cord = input("  Введите координаты через пробел: ").split()

        if len(cord) != 2:
            print("  Введите 2 координаты: ")
            continue

        a, b = cord

        if not(a.isdigit()) or not(b.isdigit()):
            print("  Введите числа! ")
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print("  Координаты вне заданного диапазона")
            continue

        if field[a][b] != " ":
            print("  Клетка занята!")
            continue

        return a, b

# Проверка выигрышных комбинаций


def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!  Сыграем ещё разок?")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!  Сыграем ещё разок?")
            return True
    return False


start()
field = [[" "]*3 for i in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья! Сыграем ещё разок!")
        break
