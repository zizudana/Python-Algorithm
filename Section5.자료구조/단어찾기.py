# n개의 단어 중 시에 쓰지 않은 단어 출력
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
note = []
poet = []
for _ in range(n):
    note.append(input())
for _ in range(n-1):
    poet.append(input())
note.sort()
poet.sort()
for i in range(n-1):
    if note[i] != poet[i]:
        break
print(note[i])