# n개의 수로 된 수열의 i번째부터 j번째 수까지의 합이 m이 되는 경우의 수 구하기

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a_sum = 0
    for j in range(i, n):
        a_sum += a_list[j]
        if a_sum == m:
            cnt += 1
            break
        if a_sum > m:
            break
print(cnt)
