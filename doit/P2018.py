n = int(input())

cnt = 1
start_idx = 1
end_idx = 1
sum = 1

while end_idx != n:
    if sum == n: #정답 조건 
        cnt += 1
        end_idx += 1
        sum += end_idx
    elif sum > n:
        sum -= start_idx
        start_idx += 1
    else: 
        end_idx += 1 
        sum += end_idx
    
print(cnt)