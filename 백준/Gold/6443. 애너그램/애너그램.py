N = int(input())

def dfs(word,wdict):
    # 종료 조건
    if len(word) == len(wlst):
        print(word)
        return

    for w in wdict:
        if wdict[w]:
            wdict[w] -= 1
            dfs(word+w, wdict)
            wdict[w] += 1

for i in range(N):
    wlst = list(input().strip())
    wlst.sort()
    # 중복 체크를 위한 dict
    wdict = {}
    for word in wlst:
        if word in wdict:
            wdict[word] += 1
        else:
            wdict[word] = 1

    dfs('',wdict)
