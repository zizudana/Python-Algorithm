# 10진수 n을 2진수로 변환하여 출력하는 프로그램

n = int(input())

def recur(num):
    if num==0:
        return
    recur(num//2)
    print(num%2, end="")

recur(n)