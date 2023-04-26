# n개의 숫자열의 s번째부터 e번째까지의 수를 오름차순 정렬했을 때 k번째 수 출력

t = int(input())
for _ in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    num = sorted(num[s-1:e])
    print(num[k-1])