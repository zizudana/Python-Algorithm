# 여러 단위의 동전들이 있을 때 거스름돈을 가장 적은 수의 동전으로 주려면 어떻게 줘야 하는가
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
coins= list(map(int, input().split()))
m = int(input())
'''
cnt= 0
coins.sort(reverse=True)
for coin in coins:
    if coin <= m and m > 0:
        cnt += m//coin
        m %= coin
    else:
        break
print(cnt)
'''
res = int(sys.maxsize)
# DFS로 풀이
def dfs(L, sum):
    global res
    if sum == m and L<res:
        res=L
    if sum > m or L>res:
        return
    else:
        for coin in coins:
            dfs(L+1, sum+coin)

dfs(0, 0)
print(res)
