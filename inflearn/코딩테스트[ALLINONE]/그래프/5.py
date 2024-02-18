def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)
    # v에 연결되어 있는 모든 vertex 방문할 것이다.
    def dfs(v):
        visited[v] =True
        for next_v in rooms[v]:
            if not visited[next_v]: # O(N)
                dfs(next_v)
    dfs(0)
    return all(visited)
    # if len(visited) == len(rooms): return True
    # else : return False

rooms = [[1,3],[2,4],[0],[4],[],[3,4]]
print(canVisitAllRooms(rooms))