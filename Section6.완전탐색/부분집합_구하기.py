# 1부터 자연수 n까지의 원소를 갖는 집합의 부분집합을 모두 출력
from itertools import combinations

n = int(input())
nums = list(range(1, n+1))
ans = []
for i in range(1, n+1):
    ans += map(list,combinations(nums, i)) 

print(ans)

def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

ch=[0]*(n+1)
DFS(1)
'''
한 원소가 포함된다/안된다 2가지 경우(상태트리)
총 경우의수=2^n -1
'''

    
    
