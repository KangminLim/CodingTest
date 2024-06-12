N = int(input())
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)
M = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)
cnt = 0
if cranes[0] < boxes[0]:
    print(-1)
else:
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                break
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        cnt += 1
    print(cnt)