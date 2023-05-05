# n명의 지원자 중 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자를 선발할 때 뽑히는 최대 인원 출력
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
players = []
for _ in range(n):
    h, w = map(int, input().split())
    players.append((h,w))

players_h = sorted(players, reverse=True)

min_weight = players_h[0][1]
cnt = 0
for h, w in players_h:
    if w < min_weight:
        continue
    cnt += 1
    min_weight = w
print(cnt)