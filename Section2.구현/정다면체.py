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

