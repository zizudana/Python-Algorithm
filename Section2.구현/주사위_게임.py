# 3개의 주사위를 던져서 상금을 받는다
# 1. 같은 눈이 3개 나오면 10000+(같은눈)*1000
# 2. 같은 눈이 2개만 나오면 1000+(같은눈)*100
# 3. 모두 다른 눈이 나오면 (가장 큰 눈)*100
# n명이 주사위 게임해서 가장 많은 상금을 받은 사람의 상금 출력
n = int(input())
dices = []
result = []
for _ in range(n):
    dices.append(list(map(int, input().split())))
for dice in dices:
    dice.sort()
    cnt = 0
    for i in range(2):
        if dice[i] == dice[i+1]:
            cnt += 1
    if cnt == 2:
        result.append(10000 + dice[1] * 1000)
    elif cnt == 1:
        result.append(1000 + dice[1] * 100)
    else:
        result.append(max(dice)*100)
print(max(result))