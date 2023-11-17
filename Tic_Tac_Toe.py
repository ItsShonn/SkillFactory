tct = [["-", "-", "-"],
       ["-", "-", "-"],
       ["-", "-", "-"]]
turn = True  # True - Крестики, False - Нолики
win = [False, None]
count = 0
print('Ходы производятся по цифрам в формате "Строчка", пробел, "Столбик"\nВыиграет тот значок, который первее '
      'соберёт свой знак в линию из трёх знаков\nЗанимать можно только свободные клетки')
def filler():
    print("----------")
def game():
    global tct,turn,win,filler,count
    this_turn = [0,0]
    if count == 9:
        return None
    if any([tct[0][0] == tct[0][1] == tct[0][2] != "-",
           tct[1][0] == tct[1][1] == tct[1][2] != "-",
           tct[2][0] == tct[2][1] == tct[2][2] != "-",
           tct[0][0] == tct[1][0] == tct[2][0] != "-",
           tct[0][1] == tct[1][1] == tct[2][1] != "-",
           tct[0][2] == tct[1][2] == tct[2][2] != "-",
           tct[0][0] == tct[1][1] == tct[2][2] != "-",
           tct[0][2] == tct[1][1] == tct[2][0] != "-"]):
        filler()
        win[0] = True
        win[1] = not (turn)
        print("  1 2 3\n1", *tct[0], "\n2", *tct[1], "\n3", *tct[2])
        filler()
        return win
    else:
        filler()
        print("  1 2 3\n1", *tct[0], "\n2", *tct[1], "\n3", *tct[2],
              "\nХод " + ("Крестиков" if turn == True else "Ноликов"))
        this_turn = input()
        if not(this_turn.replace(' ','').isdigit()):
            print("Значение должно быть числом")
            return game()
        this_turn = list(map(int, (this_turn.split())))
        if not(1 <= (this_turn[0] or this_turn[1]) <= 3):
            print("Значение не в рамках игрового поля, выбирайте индексы от 1 до 3")
            return game()
        if tct[this_turn[0]-1][this_turn[1]-1] != "-":
            print("Клетка уже занята, выберите свободную")
            return game()
        count += 1
        tct[this_turn[0]-1][this_turn[1]-1] = "x" if turn == True else "o"
        turn = not (turn)
        return tct, turn, game()
game()
if win[1] == True:
    print("Победили крестики!")
elif win[1] == False:
    print("Победили нолики!")
else:
    print("Ничья!")