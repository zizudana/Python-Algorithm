# 구명보트는 2명 이하, 총 무게 m 이하 제한
# n명의 승객이 모두 탈출하기 위한 구명보트의 최소개수 출력

n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
cnt = 0
while True:
    cnt += 1
    w = weights.pop()
    if w + weights[0] <= m:
        weights.pop(0)
    if(len(weights) == 1 or len(weights) == 0):
        break
print(cnt)

'''
deque 사용
from collections import deque
p = deque(p)
p.popleft()
p.pop()
'''