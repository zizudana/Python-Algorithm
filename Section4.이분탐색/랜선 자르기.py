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
