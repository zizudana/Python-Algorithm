# 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수 만들기
'''
조합밖에 생각이 안난당...
'''
from itertools import combinations
num, m = map(str, input().split())
removed_num = list(combinations(num, len(num)-int(m)))
removed_num.sort(reverse=True)
answer = ''.join(removed_num[0])
print(int(answer))
