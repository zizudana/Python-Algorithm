# 완성된 9*9 크기의 수도쿠가 정확하게 풀렸는지 출력
import sys
sys.stdin=open("input.txt", "rt")

board = list(list(map(int, input().split())) for _ in range(9))
check = list([0 for _ in range(11)] for _ in range(9))

flag = True
for i in range(9):
    for j in range(9):
        idx = board[i][j]
        if check[i][idx] == 0:
            check[i][idx] = 1
        else:
            flag = False
            break
    if not flag:
        break
if(flag):
    print("YES")
else:
    print("NO")

'''
행, 열, 그룹 3번 검사해야 한다

ch3[a[i*3+k][j*3+s]] = 1
'''