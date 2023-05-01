# 문자열 중 숫자만 추출하여 자연수를 만든다
# 만들어진 자연수와 그 자연수의 약수의 개수를 출력
import sys
sys.stdin=open("input.txt", "rt")

string  = input()
num = ""

for i in string:
    if '0' <= i <= '9':
        num += i
num = int(num)
print(num)

cnt = 1
for i in range(1, num//2+1):
    if num % i == 0:
        cnt += 1
print(cnt)