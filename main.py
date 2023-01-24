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

        if len(cord) !=2:
            print("  Введите 2 координаты: ")
            continue

        x, y = cord

        if not(x.isdigit()) or not(y.isdigit()):
            print("  Введите числа! ")
            continue

        x,y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 3:
            print("  Координаты вне заданного диапазона")
            continue

        if field[x][y] != " ":
            print("  Клетка занята!")
            continue

        return x, y

#Проверка выигрышных комбинаций
def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False




field=[[" "]*3 for i in range (3)]
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
