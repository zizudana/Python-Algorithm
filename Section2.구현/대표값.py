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
