import heapq
def solution(book_time):
    answer = 1
    new_bt = []
    for book in book_time:
        a = int(book[0][:2]) * 60 + int(book[0][3:])
        b = int(book[1][:2]) * 60 + int(book[1][3:])
        new_bt.append((a,b))
    new_bt.sort()
    heap = []
    for s,e in new_bt:
        if not heap:
            heapq.heappush(heap,e+10)
            continue
        if heap[0] <= s: # 현재 가장 빠른 퇴실 시간 < 입실 시간
            heapq.heappop(heap)
        else:
            answer += 1 # 새로운 방 할당
        heapq.heappush(heap,e+10)
        
    return answer