n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
apples = []
for i in range(k):
    loc = list(map(int, input().split()))
    board[loc[0]-1][loc[1]-1] = 1 #check apple's location

directions = [] #'S' = straight
dirPointer = 0
currentDir = 'right' #current direction, right, left, up, down

l = int(input())
for i in range(l):
    tmp = input().split()
    directions.append([int(tmp[0]), tmp[1]])

snake = [[0,0]] #snake's location, head goes to the end of the list => snake[-1], tail = snake[0]
board[snake[0][0]][snake[0][1]] = 2
time = 0

def printBoard(board):
    for row in board:
        print(row)
    
def nextLocation(loc, dir):
    if (dir=='up'):
        return [loc[0]-1, loc[1]]
    elif (dir=='down'):
        return [loc[0]+1, loc[1]]
    elif (dir=='left'):
        return [loc[0], loc[1]-1]
    elif (dir=='right'):
        return [loc[0], loc[1]+1]

def move(changeDir):

    global snake, board, currentDir
    #if hit, return false
    #if not, return true
    if(changeDir and changeDir == 'L'):
        if currentDir == 'up':
            currentDir = 'left'
        elif currentDir == 'down':
            currentDir = 'right'
        elif currentDir == 'left':
            currentDir = 'down'
        elif currentDir == 'right':
            currentDir = 'up'
    elif(changeDir and changeDir == 'D'):
        if currentDir == 'up':
            currentDir = 'right'
        elif currentDir == 'down':
            currentDir = 'left'
        elif currentDir == 'left':
            currentDir = 'up'
        elif currentDir == 'right':
            currentDir = 'down'

    nextLoc = nextLocation(snake[-1], currentDir)
    #out of range
    if nextLoc[0]<0 or nextLoc[0]>=n or nextLoc[1]<0 or nextLoc[1]>=n:
        return False
    #snake's body
    if board[nextLoc[0]][nextLoc[1]] == 2:
        return False
    #encounter apple
    if board[nextLoc[0]][nextLoc[1]] == 1:
        board[nextLoc[0]][nextLoc[1]] = 2
        snake.append(nextLoc) #head = nextLoc
    #encounter nothing
    if board[nextLoc[0]][nextLoc[1]] == 0 :
        board[snake[0][0]][snake[0][1]] = 0
        board[nextLoc[0]][nextLoc[1]] = 2
        snake.append(nextLoc)
        snake = snake[1:]
    return True

def everySeconds():
    global dirPointer, directions, time, board
    
    while(True):
        if dirPointer < l and directions[dirPointer][0] == time:
            if (not move(directions[dirPointer][1])):
                return time+1
            else:
                dirPointer+=1
                time+=1
        elif (not move(False)):
            return time+1
        else:
            time+=1
        
#run the main func
print(everySeconds())