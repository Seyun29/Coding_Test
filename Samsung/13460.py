import sys
#left, top, right, bottom
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dirs = ['left', 'top', 'right', 'bottom']
def next_pos(pos,dir):
    global board, n, m
    new_row = pos[0]+dx[dir]
    new_col = pos[1]+dy[dir]
    if (0 <= new_row < n) and (0 <= new_col < m):
        return new_row, new_col, board[new_row][new_col]
    return new_row, new_col, '#'

def print_board():
    global board
    for row in board:
        print(row)

sys_input = sys.stdin.readline

n,m = map(int,sys_input().split())

board = list()
red_pos, blue_pos = [-1, -1], [-1, -1]

for i in range(n):
    string = sys_input()[:-1]
    board.append(list(string))
    for k in range(m):
        if string[k] == 'R':
            red_pos = [i,k]
            board[i][k] = '.'
        elif string[k] == 'B':
            blue_pos = [i,k]
            board[i][k] = '.'

# 1. move both balls, while facing '.', if result position is same, then adjust the positions
def moveBalls(prev_red, prev_blue, dir):
    global board
    current = {
        'red': prev_red,
        'blue': prev_blue
    }
    order = ['red', 'blue']
    if dir == 0:
        order.sort(key=lambda item: current[item][1])
    elif dir == 1:
        order.sort(key=lambda item: current[item][0])
    elif dir == 2:
        order.sort(key=lambda item: current[item][1], reverse=True)
    else:
        order.sort(key=lambda item: current[item][0], reverse=True)

    for item in order:
        cur_pos = current[item]
        while next_pos(cur_pos,dir)[2] == '.':
            cur_pos = next_pos(cur_pos,dir)[:2]
        current[item] = cur_pos

    if current[order[0]] == current[order[1]]:
        current[order[1]] = [current[order[1]][0]-dx[dir], current[order[1]][1]-dy[dir]]

    return current['red'], current['blue'], True if prev_red != current['red'] or prev_blue != current['blue'] else False

results = []
def move(cnt, red_pos, blue_pos, prev_dir, paths):
    global results
    if (cnt >= 10):
        results.append(100)
        return
    cnt += 1
    for dir in range(4):
        if dir != prev_dir:
            new_red_pos, new_blue_pos, moved = moveBalls(red_pos, blue_pos, dir)
            if next_pos(new_blue_pos, dir)[2] == 'O':
                continue
            elif next_pos(new_red_pos, dir)[2] == 'O':
                if next_pos(next_pos(new_blue_pos, dir)[:2], dir)[2] != 'O':
                    results.append(cnt)
                    return
                else:
                    continue
            if not moved:
                continue
            else:
                move(cnt, new_red_pos, new_blue_pos, dir, paths)
move(0, red_pos, blue_pos, -1, [])
# print(results)
if len(results) == 0:
    print(-1)
else:
    print(-1 if min(results) > 10 else min(results))
