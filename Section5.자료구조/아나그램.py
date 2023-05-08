# 두 문자열이 알파벳의 나열 순서가 다르지만 구성이 일치하면 두 단어는 아나그램(대소문자 구별)
# 두 단어가 아나그램이면 "YES", 아니면 "NO"

word1 = sorted(input())
word2 = sorted(input())

for i in range(len(word1)):
    if word1[i] != word2[i]:
        print("NO")
        break
else:
    print("YES")
