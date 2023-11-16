T=int(input())
for t in range(1,T+1):
    text = input()
    pattern=[]
    next_pattern=[]
    ans = 0
    for i in range(1,11):
        pattern = text[:i]
        next_pattern = text[i:2*i]
        # print(pattern)
        # print(next_pattern)
        if pattern == next_pattern:
            ans=len(pattern)
            print('#{} {}'.format(t, ans))
            break

