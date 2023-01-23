Требуется написать программу, вычисляющую следующую итерацию игры «Жизнь». Игра проходит в прямоугольной области размером Nна M, состоящей из символов точка (.), 
обозначающий мёртвую клетку, и решётка (#), обозначающий живую. Новое состояние каждой клетки определяется состоянием её 8 соседей по следующим правилам:

если мёртвая клетка имеет ровно три живых соседа, она становится живой;
если живая клетка имеет меньше двух или больше трёх живых соседей, она становится мёртвой;
иначе состояние клетки не изменяется.
При этом соседями граничных клеток будут соответствующие граничные клетки с другой стороны области. Так, левым соседом самой левой клетки поля будет являться самая правая клетка в той же строке.
 
import sys
num = sys.stdin.readlines()
board = [i.rstrip() for i in num]
neighbor = []
for i in range(len(board)):
    for j in range(len(board[i])):
        neighbor.append("")
        neighbor[i * len(board[i]) + j] += board[i - 1][j]
        neighbor[i * len(board[i]) + j] += board[i - (len(board) - 1)][j]
        neighbor[i * len(board[i]) + j] += board[i][j - 1]
        neighbor[i * len(board[i]) + j] += board[i][j - (len(board[i]) - 1)]
        neighbor[i * len(board[i]) + j] += board[i - 1][j - 1]
        neighbor[i * len(board[i]) + j] += board[i - (len(board) - 1)][j - 1]
        neighbor[i * len(board[i]) + j] += board[i - 1][j - (len(board[i]) - 1)]
        neighbor[i * len(board[i]) + j] += board[i - (len(board) - 1)][j - (len(board[i]) - 1)]
        if board[i][j] == "." and neighbor[i * len(board[i]) + j].count("#") == 3:
            print("#", end='')
        elif board[i][j] == "#" and (neighbor[i * len(board[i]) + j].count("#") > 3 or neighbor[i * len(board[i]) + j].count("#") < 2):
            print(".", end="")
        else:
            print(board[i][j], end="")
    print()
