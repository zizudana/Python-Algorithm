# 환자가 접수한 순서에서 가장 앞에 있는 환자보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣는다.
# n명의 대기목록 순서의 환자 위험도가 주어지면 m번째 환자는 몇번째로 진로받는지 출력

n, m = map(int, input().split())
a = list(enumerate(map(int, input().split())))


def my_max(lists):
    ans = 0
    for i, r in lists:
        ans = max(ans, r)
    return ans


cnt = 0
while True:
    i, r = a.pop(0)
    if my_max(a) <= r:
        cnt += 1
        if i == m:
            print(cnt)
            break
    else:
        a.append((i, r))

