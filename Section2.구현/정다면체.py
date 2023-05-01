# 정N면체와 정M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 확률이 높은 숫자를 출력

from collections import Counter


n, m = map(int, input().split())
case = []
for i in range(1, n+1):
    for j in range(1, m+1):
        case.append(i+j)

case_count = Counter(case).most_common()
max_count = case_count[0][1]

for k, v in case_count:
    if v == max_count:
        print(k, end=" ")

'''
cnt = [0]*(n+m)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

최댓값 찾기
max = -2147000000
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, ent = ' ')
'''