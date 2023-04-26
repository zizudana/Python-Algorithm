# N의 약수들 중 K번째로 작은 수 출력하기
n, k = map(int, input().split())

cnt = 0
for i in range(1, n//2+1):
    if n % k == 0:
        cnt += 1
    if cnt == k:
        break
if cnt == k:
    print(i)
else:
    print(-1)