str1, str2 = input().rstrip(), input().rstrip()
l1, l2 = len(str1) + 1 ,len(str2) + 1
# 1. LCS dp 생성
LCS = [[0] * l1 for _ in range(l2)]

for i in range(1,l2):
    for j in range(1,l1):
        # 2-1. 문자가 같을 경우
        if str2[i-1] == str1[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1],LCS[i-1][j])
print(LCS[-1][-1])
