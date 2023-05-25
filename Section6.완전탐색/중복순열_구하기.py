# 1부터 n번 구슬 중 중복을 허락하여 m번 뽑아 일렬로 나열하는 방법 모두 출력
import sys
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
res = [0]*m

def dfs(L):
    if L == m:
        print(res)
        return
    else:
        for i in range(1, n+1):
            res[L] = i
            dfs(L+1)

dfs(0)