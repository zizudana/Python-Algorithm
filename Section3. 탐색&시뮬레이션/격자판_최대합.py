# n*n격자판 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
max_sum = 0
for i in range(n):
    max_sum = max(max_sum, sum(board[i]))
for i in range(n):
    board_sum = 0
    for j in range(n):
        board_sum += board[j][i]
    max_sum = max(max_sum, board_sum)
board_sum = 0
for i in range(n):
    board_sum += board[i][i]
max_sum = max(max_sum, board_sum)
board_sum = 0
for i in range(n):
    board_sum += board[i][-i-1]
max_sum = max(max_sum, board_sum)
print(max_sum)
