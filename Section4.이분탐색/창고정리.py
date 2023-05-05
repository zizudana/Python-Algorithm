# 가장 높은 곳의 상자를 가장 낮은 곳으로 이동
# m회 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력
import sys
sys.stdin=open("input.txt", "rt")

ll = int(input())
boxes = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    boxes[boxes.index(max(boxes))] -= 1
    boxes[boxes.index(min(boxes))] += 1
print(max(boxes) - min(boxes))
