import sys
from collections import deque

input_ = sys.stdin.readline

n, l, r = map(int, input_().split())
maps = []
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(n):
    maps.append(list(map(int, input_().split())))

day = 0
updated = True

def bfs(start, visited):
    global dr,dc,l,r
    union_q = deque([start])
    union = [start]
    visited[start[0]][start[1]] = 1
    while len(union_q)>0:
        row,col = union_q.popleft()
        for dir in range(4):
            next_r, next_c = row + dr[dir], col + dc[dir]
            if (0 <= next_r < n) and (0 <= next_c < n) and (l <= abs(maps[row][col] - maps[next_r][next_c]) <= r) and visited[next_r][next_c] != 1:  # if adjacent
                union_q.append([next_r,next_c])
                union.append([next_r,next_c])
                visited[next_r][next_c] = 1
    return union, visited

while True:
    unions = list()
    visited = [[0 for i in range(n)] for k in range(n)]
    for row in range(n):
        for col in range(n):
            if visited[row][col] != 1:
                union, visited = bfs([row,col], visited)
                unions.append(union)
    if len(unions) == n**2:
        break
    day += 1
    for union in unions:
        sum = 0
        for (row,col) in union:
            sum += maps[row][col]
        for (row,col) in union:
            maps[row][col] = sum // len(union)
print(day)




# # Calculate adjacent list
# adjs = []
# for r_idx in range(n):
#     for c_idx in range(n):
#         for dir_idx in range(4):
#             next_r, next_c = r_idx + dr[dir_idx], c_idx + dc[dir_idx]
#             if 0 <= next_r < n and 0 <= next_c < n:
#                 adjs.append([[r_idx, c_idx], [next_r, next_c]])

