# 후위연산식이 주어지면 연산한 결과를 출력

a = input()

stack = []
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if i == '+':
            stack.append(n2+n1)
        elif i == '-':
            stack.append(n2-n1)
        elif i == '*':
            stack.append(n2*n1)
        else:
            stack.append(n2/n1)
print(stack[0])

'''
후위식 만들기 연습

answer = ""
stack = []
for i in a:
    if i.isdecimal():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        else:
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
while stack:
    answer += stack.pop()
print(answer)
'''