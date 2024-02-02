data = input()
zero_cnt, one_cnt = 0, 0
# 첫 번째 원소에 대해 처리
if data[0] == '1':
    zero_cnt += 1
else:
    one_cnt += 1
# 두 번째 원소부터 모든 원소 확인
for i in range(len(data) -1 ):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            zero_cnt += 1
        else:
            one_cnt += 1
print(min(zero_cnt,one_cnt))