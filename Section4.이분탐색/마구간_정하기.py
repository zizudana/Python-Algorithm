# n개의 마구간에 c마리의 말을 배치할 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대값 출력
import sys
sys.stdin=open("input.txt", "rt")
from itertools import combinations

n, c = map(int, input().split())
horses = list(int(input()) for _ in range(n))
horses.sort()
cases = list(combinations(horses, 3))
max_dif = 0
for case in cases:
    min_dif = int(sys.maxsize)
    for i in range(c-1):
        min_dif = min(min_dif, case[i+1]-case[i])
    max_dif = max(max_dif, min_dif)
print(max_dif)