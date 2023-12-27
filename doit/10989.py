N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0: 
        for _ in range(count[i]): # 해당 index값만큼 idx를 반복하여 출력
            print(i)