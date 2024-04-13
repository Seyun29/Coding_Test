#BFS, DFS !!
# DFS 로직 외우기!!
import sys
from collections import deque
import copy
input_ = sys.stdin.readline

dr = [-1,1,0,0] #상하좌우
dc = [0,0,-1,1]

n,m = map(int,input_().split())
maps = list()
virus = deque()
zeros = list()
virus_cnt = 0
wall_cnt = 0
answer = 0
for row in range(n):
    l = list(map(int,input_().split()))
    maps.append(l)
    for col, e in enumerate(l):
        if e == 2:
            virus.append([row,col])
            virus_cnt += 1
        elif e == 0:
            zeros.append([row,col])
        elif e == 1:
            wall_cnt += 1

def expand_virus():
    global virus, maps, virus_cnt, wall_cnt
    old_maps = copy.deepcopy(maps)
    virus_q = virus.copy()
    total_virus_cnt = virus_cnt
    #bfs
    while len(virus_q)>0:
        v = virus_q.popleft()
        for dir in range(4):
            next_r, next_c = v[0]+dr[dir], v[1]+dc[dir]
            if (0 <= next_r < n) and (0 <= next_c < m) and maps[next_r][next_c] == 0:
                maps[next_r][next_c] = 2
                virus_q.append([next_r, next_c])
                total_virus_cnt += 1
    maps = old_maps
    return n*m - wall_cnt - 3 - total_virus_cnt

#dfs, backtracking
def dfs(idx, walls):
    global answer, maps, wall_cnt
    if walls == 3:
        answer = max(answer, expand_virus())
        return True
    elif idx == len(zeros):
        return False
    zero = zeros[idx]
    maps[zero[0]][zero[1]] = 1
    dfs(idx+1, walls+1)
    maps[zero[0]][zero[1]] = 0
    dfs(idx+1, walls)

dfs(0, 0)
print(answer)

