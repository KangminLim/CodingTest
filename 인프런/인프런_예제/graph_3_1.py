def canVisitallRooms(rooms):
    visited = [] # 5번방 방문 안했네? => False // True
    visited = set()
    # v에 연결되어 있는 모든 vertex 방문할거다.
    def dfs(v):
        visited.append(v)
        for next_v in rooms[v]:
            if next_v not in visited: # list에 쓰인 in은 memory 고갈 O(N)-> dict로
                dfs(next_v)
    dfs(0)
    return all(visited)

    if len(visited) == len(rooms) :
        return True
    else :
        return False
    # return visited
    pass

rooms = [[1,3], [2,4], [0],[4],[], [3,4]]
print(canVisitallRooms(rooms))

# //


def canVisitallRooms(rooms):
    visited = [False] * len(rooms) # 5번방 방문 안했네? => False // True
    visited = {}
    # v에 연결되어 있는 모든 vertex 방문할거다.
    def dfs(v):
        visited[v]=True
        for next_v in rooms[v]:
            if visited[next_v] == False:
                dfs(next_v)
    dfs(0)

    if len(visited) == len(rooms) :
        return True
    else :
        return False
    # return visited
    pass

rooms = [[1,3], [2,4], [0],[4],[], [3,4]]
print(canVisitallRooms(rooms))