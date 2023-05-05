# 길이 n의 수열 수열의 왼쪽 맨 끝 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 가장 긴 증가수열을 만든다

n = int(input())
arrs = list(map(int, input().split()))
before = 0
answer = ""
while len(arrs) > 0:
    if arrs[0] < before and arrs[-1] < before:
        break
    if arrs[0] < arrs[-1]:
        if arrs[0] > before:
            answer += "L"
            before = arrs.pop(0)
        elif arrs[-1] > before:
            answer += "R"
            before = arrs.pop()
    elif arrs[0] > arrs[-1]:
        if arrs[-1] > before:
            answer += "R"
            before = arrs.pop()
        elif arrs[0] > before:
            answer += "L"
            before = arrs.pop(0)
print(len(answer))
print(answer)
