# 두 리스트를 오름차순으로 합쳐 출력
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
result = n_list + m_list
result.sort()

for i in result:
    print(i, end=" ")

'''
이미 정렬된 자료이므로 O(n)으로 정렬할 수 있다.
'''