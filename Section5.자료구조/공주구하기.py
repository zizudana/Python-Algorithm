# 왕자들을 나이순으로 1번부터 n번까지 시계방향으로 동그랗게 앉힌다.
# 1번왕자부터 1부터 번호를 외쳐 한 왕자가 k를 외치면 그 왕자는 원 밖으로 나온다
# 남은 왕자 1명의 번호를 출력
# 큐 자료구조로 해결

n, k = map(int, input().split())

princes = [1]*n
cnt = 0
i = 0
while sum(princes) > 1:
    if princes[i] == 1:
        cnt += 1
        if cnt == k:
            princes[i] = 0
            cnt = 0
    i += 1
    if i == n:
        i = 0
    
for i, prince in enumerate(princes):
    if prince == 1:
        print(i+1)
        break
