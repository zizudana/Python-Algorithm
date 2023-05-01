# n*n격자판 안의 다이아몬드 모양만 수확할 때 수확하는 사과의 총 개수
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
mid = n//2
board_sum = sum(board[mid])
for i in range(mid):
    board_sum += sum(board[i][mid-i:mid+i+1])
    board_sum += sum(board[-i-1][mid-i:mid+i+1])
print(board_sum)