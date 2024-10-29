import sys
input = sys.stdin.readline
M = int(input())
tset = set()

for _ in range(M):
    cmd = str(input())
    cmd = cmd.split()
    if len(cmd) > 1:
        cmd, mul = cmd
        mul = int(mul)
    else:
        cmd = cmd[0]
    if cmd == 'add':
        if mul not in tset:
            tset.add(mul)
    elif cmd == 'remove':
        if mul in tset:
            tset.remove(mul)
    elif cmd == 'check':
        if mul in tset:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if mul not in tset:
            tset.add(mul)
        else:
            tset.remove(mul)
    elif cmd == 'all':
        tset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif cmd == 'empty':
        tset = set()
