# n명의 학생들의 평균점수(소수 첫째짜리 반올림)
# n명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력
n = int(input())
score = list(map(int, input().split()))
min_dif = max(score)+1
score_avg = int(round(sum(score) / len(score),0))
before_score = min(score)-1
for i in range(n):
    if score[i] > score_avg:
        dif = score[i] - score_avg
    else:
        dif = score_avg - score[i]
    if dif <= min_dif and before_score < score[i]:
        answer = i
        min_dif = dif
        before_score = score[i]
print(score_avg, answer+1)

'''
소수 첫째 자리에서 반올림
파이썬의 round는 round_half_even방식을 택한다.
->4.5000의 경우 5가 아닌 짝수 4로 반올림한다.
round_half_up 계산법
a = 4.5
a = int(a+0.5)
'''

'''
min = -2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
'''