# n*n격자판 격자의 행을 기준으로 왼쪽 또는 오른쪽으로 회전
# 행번호 방향(0:왼쪽 1:오른쪽) 회전수
# m개의 회전명령 실행 후 모래시계 영역에 감이 몇개 있는지 출력
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
m = int(input())
for _ in range(m):
    a, b, c = map(int,input().split())
    if b==0:
        board[a-1] = board[a-1][m%n:] + board[a-1][:m%n]
    else:
        board[a-1] = board[a-1][-m%n-1:] + board[a-1][:-m%n-1]
        
mid = n//2
board_sum = board[mid][mid]
for i in range(mid):
    board_sum += sum(board[i][i:n-i])
    board_sum += sum(board[-i-1][i:n-i])
print(board_sum)