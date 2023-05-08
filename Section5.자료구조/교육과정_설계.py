# 필수과목은 순서대로 모두 이수해야 한다.
# 수업설계가 주어지면 잘된것이면 YES, 잘못된것이면 NO를 출력
import sys
sys.stdin=open("input.txt", "rt")
mandatory = input()
n = int(input())
lessons = []
for i in range(n):
    lessons.append(input())

for lesson in lessons:
    i, j = 0, 0
    while i < len(mandatory) and j < len(lesson):
        if lesson[j] == mandatory[i]:
            i += 1
        j += 1
    if i != len(mandatory):
        print("NO")
    else:
        print("YES")