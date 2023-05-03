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

'''
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
all() 조건이 모두 참일때 참
if all(a[i][j]>a[i+dx[k]][j+dy[k]]) for k in range(4) 
'''

