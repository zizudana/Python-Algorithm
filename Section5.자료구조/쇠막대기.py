# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 한다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
# 레이저 () 쇠막대기 왼쪽끝 ( 오른쪽끝 ) 
# 쇠막대기는 레이저에 의해 몇개의 조각으로 잘리는지 총 조각 개수 구하기

strs = input()
stack = []
cnt = 0
for i, s in enumerate(strs):
    if s == '(':
        stack.append('(')
    elif s == ')':
        if strs[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)

'''
여는 괄호는 스택에 넣는다.
닫는 괄호를 만나면 레이저인지 확인하고 레이저이면 스택에 있는 수 만큼 카운트
레이저가 아닌 닫는 괄호는 1만 더해준다
'''