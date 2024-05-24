n,k = map(int, input().split())
lectures = list()
for i in range(n):
    w,s,e= map(int, input().split())
    if w != 5:
        lectures.append([w,s,e])
len_lectures = len(lectures);
time_table=[[False for i in range(11)] for i in range(6)] #w : 1~5, s,e: 1~10
def getCredit(s,e):
    return e-s+1

def isReserved(w,s,e):
    for t in range(s,e+1):
        if time_table[w][t]:
            return True
    return False

def reserve(w,s,e):
    for t in range(s,e+1):
        time_table[w][t] = True

def free(w,s,e):
    for t in range(s,e+1):
        time_table[w][t] = False

count = 0
def recur(idx, sum):
    global len_lectures, count, k
    if sum == k:
        count += 1
        return
    elif idx >= len_lectures or sum > k:
        return
    w,s,e = lectures[idx]
    if (not isReserved(w,s,e)):
        reserve(w,s,e)
        recur(idx+1,sum+getCredit(s,e))
        free(w,s,e)
    recur(idx+1,sum)

recur(0, 0)
print(count)




