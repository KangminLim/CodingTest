# 수 묶기
from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one, zero = 0, 0

for i in range(N): # 4가지로 데이터 분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1) # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minusPq.put(data)

sum = 0

while plusPq.qsize() > 1:
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second

if plusPq.qsize() > 0:
    sum += plusPq.get() * -1

while minusPq.qsize() > 1:
    first = plusPq.get()
    second = plusPq.get()
    sum += first * second

if minusPq.qsize() > 0:
    if zero == 0 :
        sum += minusPq.get()

sum += one
print(sum)