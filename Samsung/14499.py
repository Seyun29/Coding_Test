import sys
import copy
#list.copy() => shallow
#import copy => copy.deepcopy(obj)!!!!***
input_ = sys.stdin.readline

n,m,x,y,k = map(int,input_().split())
maps = list()
for i in range(n):
    maps.append(list(map(int,input_().split())))
dirs = list(map(int,input_().split()))
dx,dy=[0,0,-1,1],[1,-1,0,0] #EWSN
dice = [[-1,0,-1],
        [0,0,0],
        [-1,0,-1],
        [-1,0,-1]]

def rotate_dice(dir):
    #deep copy
    global dice
    new_dice = copy.deepcopy(dice)
    if dir == 1:
        new_dice[1][1] = dice[1][2]
        new_dice[1][0] = dice[1][1]
        new_dice[1][2] = dice[3][1]
        new_dice[3][1] = dice[1][0]
    elif dir == 2:
        new_dice[1][2] = dice[1][1]
        new_dice[1][1] = dice[1][0]
        new_dice[3][1] = dice[1][2]
        new_dice[1][0] = dice[3][1]
    elif dir == 3:
        new_dice[1][1] = dice[0][1]
        new_dice[2][1] = dice[1][1]
        new_dice[3][1] = dice[2][1]
        new_dice[0][1] = dice[3][1]
    elif dir == 4:
        new_dice[0][1] = dice[1][1]
        new_dice[1][1] = dice[2][1]
        new_dice[2][1] = dice[3][1]
        new_dice[3][1] = dice[0][1]
    dice = new_dice
    return dice[1][1] #Bottom plane

def move(dir):
    global x,y,dice
    next_x = x+dx[dir-1]
    next_y = y+dy[dir-1]
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
        return False
    x,y = next_x, next_y
    bottom = rotate_dice(dir)
    if maps[x][y] == 0:
        maps[x][y] = bottom
    else:
        dice[1][1] = maps[x][y]
        maps[x][y] = 0
    print(dice[3][1])
    # print('updated coord ---')
    # print(x, y)
    # print('MAP ---')
    # for row in maps:
    #     print(row)
    # print('DICE ---')
    # for row in dice:
    #     print(row)

    return True


for dir in dirs:
    move(dir)






