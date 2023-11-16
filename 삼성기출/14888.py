
def dfs(n,sm,add,sub,mul,div):
    global mn,mx
    # [0] 결과값/ 중간값 범위는 int(1e8),-int(1e8)
    if sm<int(-1e8) or int(1e8)<sm:
        return
    if n==N:
        mn = min(mn,sm)
        mx = max(mx,sm)
        return
    if add>0:
        dfs(n+1,sm+lst[n],add-1,sub,mul,div)
    if sub>0:
        dfs(n+1,sm-lst[n],add,sub-1,mul,div)
    if mul>0:
        dfs(n+1,sm*lst[n],add,sub,mul-1,div)
    if div>0:
        dfs(n+1,sm/lst[n],add,sub,mul,div-1)


N = int(input())
lst = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())
mn,mx = int(1e8),-int(1e8)
dfs(1,lst[0],add,sub,mul,div)
print(mx,mn, sep='\n')