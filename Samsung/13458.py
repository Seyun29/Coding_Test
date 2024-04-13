import sys
input_ = sys.stdin.readline

n = int(input_())
a = list(map(int,input_().split()))
b,c = map(int,input_().split())

total = n
for i in a:
    if i-b>0:
        total+=(i-b+c-1)//c
print(total)
