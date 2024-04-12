# start = (start - 1) %(2*N)
# end = (end -1) % (2*N)
# Deque => popleft, append, popright, appendleft...
import sys
from collections import deque

read = sys.stdin.readline

n,k = map(int, read().split())
weight = list(map(int, read().split()))
robots = list(0 for i in range(2*n))
robot_q = deque()

zeros = 0
load, unload = 0, n-1

# class Nodes: {
#    init()
# }
step = 0

def moveit(idx, unload):
    global weight, robots, zeros
    next_pos = (idx + 1) % (2 * n)
    if weight[next_pos] > 0 and robots[next_pos] == 0 and robots[idx] == 1:
        # and (robots[idx] == 1)
        weight[next_pos] -= 1
        if weight[next_pos] <= 0:
            zeros += 1
        robots[idx] = 0
        # 내리는 칸인 경우 즉시 하차이므로
        if next_pos == unload:
            robots[next_pos] = 0
        else:
            robots[next_pos] = 1

while(zeros < k):
    step += 1
    #올리는 위치가 index=0에서부터 뒤로 한칸씩 밀린다. 내리는 위치도 마찬가지
    load = load - 1 if load != 0 else 2*n - 1
    unload = unload - 1 if unload != 0 else 2*n - 1
    #unload robots
    robots[unload] = 0
    new_robot_q = deque()
    #move robots (robots index+1)
    #Unload에서 무조건 내린다고 가정

    # load ... unload => unload ~ load까지만
    # unload ... load =>
    if unload > load:
        for idx in range(unload, load-1, -1):
            moveit(idx, unload)
    else:
        for idx in range(unload, -1, -1):
            moveit(idx, unload)
        for idx in range(2*n-1, load - 1, -1):
            moveit(idx, unload)

    robot_q = new_robot_q
    #load robots
    if weight[load] > 0:
        robots[load] = 1
        robot_q.append(load)
        weight[load] -= 1
        if (weight[load] <= 0):
            zeros+=1

print(step)