# 큰 수의 법칙 (M이 매우 작을 때)
N,M, K = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        M -= 1 #더할 때마다 1씩 빼기
    if M ==0: #m이 0이라면 반복문 탈출
        break
    result += second #두 번째로 큰수를 한 번 더하기
    M -= 1 #더할 때마다 1씩 빼기

print(result)
