from collections import defaultdict
import math
M, N = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(M)]
idict = defaultdict(int)

for items in lst:
    items = {item : i for i,item in enumerate(items)}
    # print(items)
    index = [items[i] for i in sorted(items.keys())]
    # print(index)
    key = ''.join(list(map(str,index)))
    # print(key)
    idict[key] += 1

ans = 0

for key in idict:
    if idict[key] > 1:
        ans += math.comb(idict[key],2)

print(ans)
