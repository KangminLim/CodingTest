N = int(input())
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)
M = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)
cnt = 0
i = 0

# 모든 박스를 배로 못 옮길 경우
if cranes[0] < boxes[0]:
    print(-1)
else:
    # 박스를 다 옮기면 종료
    while boxes:
        # 가장 무거운 크레인부터
        for crane in cranes:
            # 박스를 다 옮기지 못하고 남은 크레인으로 옮길 박스가 없을 때
            if boxes and crane < boxes[-1]:
                break
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        cnt += 1

    print(cnt)