# n개의 수 오름차순 정렬
# 이분검색으로 m이 몇 번째에 있는지 구하기

import sys
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = 0
e = n-1
while(s <= e):
    mid = s + (e - s)//2
    if nums[mid] == m:
        print(mid+1)
        break
    if nums[mid] < m:
        s = mid+1
    else:
        e = mid-1
