# k개 랜선을 잘라 길이가 같은 n개 랜선 만들 때 만들 수 있는 최대 랜선 길이 구하기
import sys
sys.stdin=open("input.txt", "rt")

k, n = map(int, input().split())
lens = []
for _ in range(k):
    lens.append(int(input()))
max_len = min(lens)
while(True):
    cnt = 0
    for len in lens:
        cnt += len // max_len
    if cnt >= n:
        break
    max_len -= 1
print(max_len)

'''
결정알고리즘
1~1000 사이이므로 500으로 확인
1~499 사이이므로 250으로 확인
1~249 사이이므로 125로 확인 -> 가능
126~249 사이 187 확인 -> 가능
188~249 사이 ...
'''