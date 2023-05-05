# n개의 회의 겹치지 않게 회의실을 사용할 수 있는 최대수의 회의 구하기
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s,e))

times.sort(key=lambda x: x[1])

end = times[0][1]
cnt = 1
for i in range(1, n):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]
print(cnt)