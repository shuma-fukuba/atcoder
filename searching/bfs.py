from collections import deque

def bfs(sy: int, sx: int, gy: int, gx: int, stage: list[list[str]], visited: list[list[int]]) -> int:
    visited[sy][sx] = 0
    Q = deque([])
    Q.append([sy, sx])

    while Q:
        y, x = Q.popleft()
        if [y, x] == [gy, gx]:
            return visited[gy][gx]

        for i, j in [(-1,0), (0, -1), (1, 0), (0, 1)]:
            if stage[y + i][x + j] == '.' and visited[y + i][x+j] == -1:
                visited[y+i][x+j] = visited[y][x] + 1
                Q.append([y+i, x+j])
