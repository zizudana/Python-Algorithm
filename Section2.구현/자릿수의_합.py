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

