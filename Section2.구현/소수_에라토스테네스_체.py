# 1부터 N까지의 소수의 개수를 출력
n = int(input())
cnt = 0
for num in range(2, n):
    flag = 1
    for i in range(2, num//2+1):
        if num % i == 0:
            flag = 0
            break
    if flag:
        cnt += 1
print(cnt)