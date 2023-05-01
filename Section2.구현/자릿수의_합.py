# n개 자연수의 자릿수의 합 구하고 그 합이 최대인 자연수 출력
def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

n = int(input())
nums = list(map(str, input().split()))
result = []
for num in nums:
    result.append(digit_sum(num))
max_result = max(result)
for i in range(n):
    if result[i] == max_result:
        break
print(nums[i])

'''
각 자릿수의 합 구하기
def digit_sum(x):
    sum = 0
    정수처리
    while x>0:
        sum += x%10
        x = x//10
    return sum
    
    문자열취급
    for i in str(x):
        sum += int(i)        
'''