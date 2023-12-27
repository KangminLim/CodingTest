from queue import PriorityQueue
import sys
print=sys.stdout.write
input = sys.stdin.readline
N= int(input())
myQueue=PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp=myQueue.get()
            print(str((temp[1]))+'\n')
    else: 
        myQueue.put((abs(request),request))