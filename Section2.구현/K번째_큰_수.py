# n장의 카드 중 3장을 뽑아 각 카드 숫자의 합을 기록
# 기록한 값 중 k번째로 큰 수를 출력
from itertools import combinations

n, k = map(int, input().split())
card = list(map(int, input().split()))
card.sort(reverse=True)
card3 = list(combinations(card, 3))
print(sum(card3[k-1]))