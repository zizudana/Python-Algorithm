# n*n 격자판 숫자 중 상하좌우 숫자보다 큰  숫자는 봉우리 지역
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
board = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+1):
    board[i][1:n] = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] > max(board[i-1][j], board[i+1][j], board[i][j-1], board[i][j+1]):
            cnt += 1
print(cnt)

