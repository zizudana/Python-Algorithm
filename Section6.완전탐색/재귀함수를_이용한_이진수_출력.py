# 10진수 n을 2진수로 변환하여 출력하는 프로그램

n = int(input())
ans = []
def recur(num):
    if num==0:
        return
    ans.append(num%2)
    recur(num//2)

recur(n)
for i in reversed(ans):
    print(i, end="")