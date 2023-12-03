print("___Крестики-нолики___")

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board(board):
    for i in range(3):
        print("-" * 13)
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("-" * 13)


def player_move(x_or_o):
    flag = False
    while not flag:
        answer = input("Назовите число куда ставим " + x_or_o + "?")
        try:
            answer = int(answer)
        except:
            print("Вы ввели не число.")
            continue
        if 1 <= answer <= 9:
            if str(board[answer - 1]) not in "XxOo0":
                board[answer - 1] = x_or_o
                flag = True
            else:
                print("Эта клетка уже занята.")
        else:
            print("Вы ввели число больше 9 или меньше 1.")


def win_code(board):
    win_combination = (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), \
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)

    for el in win_combination:
        if board[el[0]] == board[el[1]] == board[el[2]]:
            return board[el[0]]





if __name__ == "__main__":
    draw_board(board)
    count = 0
    win = False
    while not win:
        if count % 2 == 0:
            player_move("X")
        else:
            player_move("0")
        count += 1

        if count > 4:
            winner = win_code(board)
            if winner:
                print(winner, "выиграл!")
                win = True
        if count == 9:
            print("Ничья")
            win = True
        draw_board(board)
