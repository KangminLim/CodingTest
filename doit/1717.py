# 집합 표현하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int,input().split())
parent = [0] * (N+1)

# find 연산
def find(a):
    if a == parent[a]:
        return a
    else:
        # 재귀 형태로 구형 -> 경로 압축 부분
        parent[a] = find(parent[a])
        return parent[a]

# union 연산 / 대표 노드끼리 합치기
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0, N+1):
    parent[i] = i

for i in range(M):
    question, a, b= map(int,input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")