import sys
input = sys.stdin.readline

N = int(input())
graph = [0] + [int(input()) for _ in range(N)]
answer = []

def dfs(cur,start):
    v[cur] = True
    w = graph[cur]
    if not v[w]:
        dfs(w,start)
    elif v[w] and w == start:
        answer.append(w)

for i in range(1,N+1):
    v = [False] * (N+1)
    dfs(i,i)

print(len(answer))
answer.sort()

for i in answer:
    print(i)