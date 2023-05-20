# 1부터 자연수 n까지의 원소를 갖는 집합의 부분집합을 모두 출력
from itertools import combinations

n = int(input())
nums = list(range(1, n+1))
ans = []
for i in range(1, n+1):
    ans += map(list,combinations(nums, i)) 

print(ans)