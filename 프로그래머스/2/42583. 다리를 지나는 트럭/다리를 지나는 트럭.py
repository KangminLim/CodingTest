from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    cur_weight = 0
    while truck and bridge:
        time += 1
        cur_weight -= bridge.popleft()
        if cur_weight + truck[0] <= weight:
            cur_weight += truck[0]
            bridge.append(truck.popleft())
        else:   
            bridge.append(0)
    
    time += bridge_length
    return time