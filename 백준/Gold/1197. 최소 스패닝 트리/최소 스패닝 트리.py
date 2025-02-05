import sys
from queue import PriorityQueue
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N,M = map(int,input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    s, e, w = map(int,input().split())
    pq.put((w,s,e))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N-1: # MST는 항상 N-1의 에지를 사용함
    w, s, e = pq.get()
    if find(s) != find(e): # 같은 부모가 아닌 경우만 연결
        union(s,e)
        result += w
        useEdge += 1

print(result)

