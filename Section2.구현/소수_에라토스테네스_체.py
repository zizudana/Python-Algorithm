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

'''
에라토스테네스 체
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)
'''