H, W = map(int,input().split())
world = list(map(int,input().split()))
ans = 0
# i 번째 고이는 물 구하기 
for i in range(1,W-1):
    l_mx = max(world[:i])
    r_mx = max(world[i+1:])

    cur = min(l_mx,r_mx)

    if world[i] < cur:
        ans += (cur-world[i])
print(ans)