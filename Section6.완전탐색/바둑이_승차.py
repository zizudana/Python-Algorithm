# 트럭은 c킬로그램 넘게 태울 수 없다
# n마리의 바둑이와 각 바둑이의 무게 w 일때 트럭에 태울 수 있는 가장 무거운 무게 구하기

import sys
sys.stdin=open("input.txt", "rt")


def DFS(v, s, tsum):
    global max_s
    if s+(total-tsum) < max_s:
        return
    if s > c:
        return
    if v==n:
        max_s = max(max_s, s)
    else:
        DFS(v+1, s+w[v], tsum+w[v])
        DFS(v+1, s, tsum+w[v])

c, n = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))
max_s = 0
total = sum(w)
DFS(0, 0, 0)
print(max_s)

'''
최적화 - 남은 것들을 다 더해도 현재 max값보다 작으면 더 해볼 필요가 없음
'''