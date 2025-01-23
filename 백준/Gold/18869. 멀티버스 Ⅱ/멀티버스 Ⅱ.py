import sys, math
from collections import defaultdict
input = sys.stdin.readline

M, N = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]

idict = defaultdict(int)

for items in lst:
    items = {item : i for i, item in enumerate(items)}
    # print(items)
    index = [items[item] for item in sorted(items.keys())]
    # print(index)
    key = ''.join(list(map(str,index)))
    # print(key)
    idict[key] += 1
    # print(idict)

answer = 0
for index in idict:
    if idict[index] > 1:
        answer += math.comb(idict[index],2)
print(answer)