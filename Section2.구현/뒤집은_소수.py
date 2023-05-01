# n개의 자연수를 뒤집은 후 뒤집은 수가 소수이면 그 수를 출력
def reverse(x): # 뒤집는 함수
    return int(x[::-1])

def isPrime(x): # 소수판별함수
    if x==1:
        return False
    flag = 1
    for i in range(2, x//2+1):
        if x % i == 0:
            flag = 0
            break
    if flag:
        return True
    else:
        return False

n = int(input())
nums = list(map(str, input().split()))
for num in nums:
    if isPrime(reverse(num)):
        print(reverse(num), end=" ")
        
'''
def reverse(x):
    res = 0
    while x>0:
        t=x%10
        res = res*10+t
        x=x//10
    return res
'''