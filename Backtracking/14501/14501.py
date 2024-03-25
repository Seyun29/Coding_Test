import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

maxx = 0
def calc(idx, sum):
    # idx -> idx of the array, starts with 0
    # sum -> sum of the values so far
    global maxx
    # return condition
    if (idx >= n):
        if (sum > maxx):
            maxx = sum
        return
    # return conditon 2 : idx+arr[idx][0] > len(arr)인 경우 포함하면 안됨
    # idx+arr[idx][0] = len(arr) 인 경우, idx+arr[idx][0] - 1 < n
    if (idx+arr[idx][0] <= n): #지금 날짜 + 수행시간 = 10
        # idx인덱스를 포함할 경우
        calc(idx + arr[idx][0], sum + arr[idx][1])
    # idx인덱스를 포함하지 않을 경우
    calc(idx+1, sum)

calc(0, 0)
print(maxx)
