# 1부터 n까지 각각의 수 앞에 놓여있는 자신보다 큰 숟들의 개수를 역수열
# 역수열이 주어질 때 원래의 수열을 출력

n = int(input())
re_arrs = list(map(int, input().split()))

arrs = [0]*(n+1)
for i in range(n):
    num = re_arrs[i]
    cnt = 0
    for idx in range(1, n+1):
        if arrs[idx] == 0:
            cnt += 1
        if cnt == num+1:
            break
    arrs[idx] = i+1
print(arrs)

for i in range(1, n+1):
    print(arrs[i], end=" ")