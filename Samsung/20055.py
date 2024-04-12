# start = (start - 1) %(2*N)
# end = (end -1) % (2*N)
# Deque => popleft, append, popright, appendleft...
# enumerate, zip
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
while(zeros < k):
    step += 1
    #올리는 위치가 index=0에서부터 뒤로 한칸씩 밀린다. 내리는 위치도 마찬가지
    load = load - 1 if load != 0 else 2*n - 1
    unload = unload - 1 if unload != 0 else 2*n - 1
    #unload robots
    robots[unload] = 0
    new_robot_q = deque()
    #move robots (robots index+1)
    for i in range(len(robot_q)):
        idx = robot_q.popleft()
        next_pos = idx + 1 if idx != 2*n - 1 else 0
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
                new_robot_q.append(next_pos)
        else:
            new_robot_q.append(idx)

    robot_q = new_robot_q
    #load robots
    if weight[load] > 0:
        robots[load] = 1
        robot_q.append(load)
        weight[load] -= 1
        if (weight[load] <= 0):
            zeros+=1

for idx in range(10,1,-1):
    print(idx)

print(step)