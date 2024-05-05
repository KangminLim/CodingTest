import sys
input = sys.stdin.readline

N = int(input())
total = 0
for _ in range(N) :
    total += int(input())

print(total - (N-1))