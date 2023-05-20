# 트럭은 c킬로그램 넘게 태울 수 없다
# n마리의 바둑이와 각 바둑이의 무게 w 일때 트럭에 태울 수 있는 가장 무거운 무게 구하기

import sys
sys.stdin=open("input.txt", "rt")


def DFS(v, s):
    global max_s
    if s > c:
        return
    if v==n:
        max_s = max(max_s, s)
    else:
        DFS(v+1, s+w[v])
        DFS(v+1, s)

c, n = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))
max_s = 0
DFS(0, 0)
print(max_s)