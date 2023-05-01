# n개의 문자열이 앞에서 읽을때나 뒤에서 읽을때나 같은 경우(회문문자열) YES출력, 아니면 NO출력
# 대소문자를 구분하지 않는다.
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
words = []
for _ in range(n):
    words.append(input().lower())
for word in words:
    flag = True
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

'''
if s==s[::-1]로 간단하게 검사 가능
'''