import sys
from collections import Counter
input = sys.stdin.readline
N, M =map(int,input().split())
lst = list(map(int,input().split()))

count = Counter(lst)
unique_nums = sorted(count.keys())

current_sequence = []

def bt():
    if len(current_sequence) == M:
        print(' '.join(map(str,current_sequence)))
        return

    for num in unique_nums:
        if count[num] > 0:
            count[num] -= 1
            current_sequence.append(num)
            bt()
            current_sequence.pop()
            count[num] += 1
bt()

