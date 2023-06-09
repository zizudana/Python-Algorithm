# 이진트리를 전위순회와 후위순회 연습(깊이우선탐색)
'''
전위 - 부모 왼쪽 오른쪽
중위 - 왼쪽 부모 오른쪽
후위 - 왼쪽 오른쪽 부모
'''

def DFS(v):
    if v>7:
        return
    else:
        print(v)
        # 전위순회
        DFS(v*2) # 왼쪽노드호출
        # 중위순회
        DFS(v*2+1) # 오른쪽노드호출
        # 후위순회

DFS(1)