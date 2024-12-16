S = str(input())

zcnt = ocnt = 0
if S[0] == '0':
    ocnt += 1
else:
    zcnt += 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            zcnt += 1
        elif S[i+1] == '0':
            ocnt += 1
print(min(zcnt,ocnt))