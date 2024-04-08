import sys
#left, top, right, bottom, nothing
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sysInput = sys.stdin.readline

n,m = map(int,sysInput().split())

board = list()
redPos, bluePos, holePos = [-1, -1], [-1, -1], [-1, -1]

for i in range(n):
    string = sysInput()[:-1]
    board.append(list(string))
    for k in range(m):
        if string[k] == 'R':
            redPos = [i,k]
            board[i][k] = '.'
        elif string[k] == 'B':
            bluePos = [i,k]
            board[i][k] = '.'
        elif string[k] == 'O':
            holePos = [i,k]

minCnt = 10
def moveOnce(dir, redPos, bluePos):
    newRed, newBlue = redPos, bluePos
    global board

    if bluePos[0]+dx[dir] == redPos[0] and bluePos[1]+dy[dir] == redPos[1]:
        if board[redPos[0]+dx[dir]][redPos[1]+dy[dir]] == '.':
            new_Red, newBlue = [redPos[0]+dx[dir], redPos[1]+dy[dir]], [bluePos[0]+dx[dir], bluePos[1]+dy[dir]]
        elif board[redPos[0]+dx[dir]][redPos[1]+dy[dir]] == 'O':
            #Red가 빠진 경우 (성공)
            return 'success'
        else:
            return False

    elif redPos[0]+dx[dir] == bluePos[0] and redPos[1]+dy[dir] == bluePos[1]:
        if board[bluePos[0]+dx[dir]][bluePos[1]+dy[dir]] == '.':
            newRed, newBlue = [redPos[0]+dx[dir],redPos[1]+dy[dir]], [bluePos[0]+dx[dir], bluePos[1]+dy[dir]]
        elif board[bluePos[0]+dx[dir]][bluePos[1]+dy[dir]] == 'O':
            #Blue가 빠진 경우 (실패)
            return 'fail'
        else:
            return False

    else:
        if board[bluePos[0] + dx[dir]][bluePos[1] + dy[dir]] == 'O':
            #blue가 빠진 경우 (실패)
            return 'fail'
        elif board[redPos[0] + dx[dir]][redPos[1] + dy[dir]] == 'O':
            #red가 빠진 경우 (성공)
            return 'success'
        if board[bluePos[0]+dx[dir]][bluePos[1]+dy[dir]] == '.':
            newBlue = [bluePos[0]+dx[dir], bluePos[1]+dy[dir]]
        if board[redPos[0]+dx[dir]][redPos[1]+dy[dir]] == '.':
            newRed = [redPos[0]+dx[dir], redPos[1]+dy[dir]]
        elif board[bluePos[0]+dx[dir]][bluePos[1]+dy[dir]] == '#' and board[redPos[0]+dx[dir]][redPos[1]+dy[dir]] == '#':
            return False

    return newRed, newBlue

def move(curCnt, redPos, bluePos, prevDir):
    global board, minCnt
    curRed, curBlue = redPos, bluePos
    if (curCnt>=10):
        return False

    for dir in range(4):
        if dir != prevDir:
            #끝까지 이동
            while(True):
                res = moveOnce(dir, curRed, curBlue)
                if res == 'success':
                    minCnt = min(minCnt, curCnt + 1)
                    return True
                elif not res:
                    #공 두개가 더 이상 움직일 수 없는 경우
                    break
                elif res == 'fail':
                    #파란공이 빠진 경우
                    return False
                else:
                    curRed, curBlue = res[0], res[1]

            if (curRed != redPos or curBlue != bluePos):
                move(curCnt + 1, curRed, curBlue, dir)

            elif not res:
                return False
            else:
                move(curCnt+1, res[0], res[1], dir)

move(0, redPos, bluePos, -1)
print(-1 if minCnt >= 10 else minCnt)