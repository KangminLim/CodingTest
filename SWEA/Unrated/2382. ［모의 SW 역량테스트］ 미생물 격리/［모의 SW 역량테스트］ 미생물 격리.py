T = int(input())
di,dj = [0,-1,1,0,0],[0,0,0,-1,1]
opp = {1:2,2:1,3:4,4:3}
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    tlst = []
    for _ in range(1, K + 1):
        ci, cj, cp, cd = map(int, input().split())
        tlst.append((ci, cj, cp, cd))
    for turn in range(1,M+1):
        # 1. 미생물 이동
        for i in range(len(tlst)):
            ci,cj,cp,cd = tlst[i]
            ni,nj = ci+di[cd],cj+dj[cd]
            if 1<=ni<=N-2 and 1<=nj<=N-2:
                tlst[i] = (ni,nj,cp,cd)
            else:
                cp = int(cp//2)
                cd = opp[cd]
                tlst[i] = (ni,nj,cp,cd)

        tlst.sort(key=lambda x:(x[0],x[1],-x[2]))
        tlst.append((101,101,0,9))

        nlst = []
        i = 0
        while i < len(tlst)-1:
            ci,cj,cp,cd = tlst[i]

            for j in range(i+1,len(tlst)):
                ti,tj,tp,td = tlst[j]
                if (ci,cj) == (ti,tj):
                    cp += tp
                else:
                    nlst.append((ci,cj,cp,cd))
                    i = j
                    break
        tlst = nlst
    ans = 0
    for i in range(len(tlst)):
        ans += tlst[i][2]
    print(f'#{tc}', ans)

