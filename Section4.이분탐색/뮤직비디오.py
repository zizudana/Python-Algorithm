# n개의 곡을 m개의 dvd에 모두 녹화하기 위해 필요한 최소 용량 크기
import sys
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
songs = list(map(int, input().split()))
min_size = max(songs)
while(True):
    cnt = 1
    size_cnt = 0
    for i in range(n):
        size_cnt += songs[i]
        if size_cnt > min_size:
            size_cnt = songs[i]
            cnt += 1
    if cnt <= m:
        print(min_size)
        break
    min_size += 1
