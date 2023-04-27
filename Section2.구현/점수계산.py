# 처음 맞는 문제는 1점
# 연속으로 두번째 문제는 2점, 세번째 문제는 3점, ..., k번째는 k점
# 틀린문제는 0점
# 시험문제의 채점결과를 통해 총 점수 계산
n = int(input())
scores = list(map(int, input().split()))
bonus = 0
total = 0
for score in scores:
    if score:
        bonus += 1
        total += bonus
    else:
        bonus = 0
print(total)
