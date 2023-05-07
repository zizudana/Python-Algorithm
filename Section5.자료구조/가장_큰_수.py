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

'''
앞에서부터 이전까지 숫자 중 자신보다 작은 수를 m번까지 지운다.
'''
stack = []
cnt = int(m)
for i in num:
    while True:
        if len(stack) > 0 and cnt > 0 and int(stack[-1]) < int(i):
            stack.pop()
            cnt -= 1
        else:
            break
    stack.append(i)
if cnt != 0:
    stack = stack[:-cnt]
answer = ''.join(stack)
print(answer)
