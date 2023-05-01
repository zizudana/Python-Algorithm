# 1부터 20까지 숫자가 쓰인 카드 오름차순으로 놓는다
# 구간 [a, b] : 위치 a부터 b까지 카드를 현재의 역순으로 놓는다
# 10개의 구간이 주어지면 순서대로 작업하고 마지막 배치를 구한다
import sys
sys.stdin=open("input.txt", "rt")

card = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    new_card = card[a-1:b]
    card = card[:a-1] + new_card[::-1] + card[b:]

print(card)

'''
swap으로 뒤집을 수 있다.
a, b = b, a

a=list(range(21))
'''