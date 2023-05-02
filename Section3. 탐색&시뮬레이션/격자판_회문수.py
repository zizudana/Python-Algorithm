# 7*7 격자판 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하기
import sys
sys.stdin=open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for mid in range(2, 5):
        if board[i][mid-1] == board[i][mid+1] and board[i][mid-2] == board[i][mid+2]:
            cnt += 1
        if board[mid-1][i] == board[mid+1][i] and board[mid-2][i] == board[mid+2][i]:
            cnt += 1
print(cnt)


