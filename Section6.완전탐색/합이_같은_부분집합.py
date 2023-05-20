# n개의 원소로 구성된 자연수 집합을 두 개의 부분집합으로 나누었을 때 원소의 합이 서로 같은 경우가 존재하면 YES출력
# 둘로 나뉘는 두 부분집합은 서로소집합, 두 부분집합을 합하면 원래 집합이 되어야 한다.
import sys
sys.stdin=open("input.txt", "rt")

def DFS(v, s):
    if s>total//2:
        return
    if v==n:
        if s == (total-s):
            print("YES")
            sys.exit(0)
    else:
        DFS(v+1,s+arr[v])
        DFS(v+1,s)

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
if total%2==1:
    print("NO")
else:
    DFS(0, 0)
    print("NO")
'''
총합이 홀수면 같을 수 없다.
중간에 s가 total//2보다 크면 return
'''