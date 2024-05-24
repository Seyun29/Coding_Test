from functools import cmp_to_key

l = [1,2,3,4]
def comparator(a,b):
    if a<b:
        #정렬기준 앞에올 조건
        return 1
    elif a>b:
        #정렬기준 반대로 뒤로갈 조건
        return -1
    else :
        #[정렬기준에 해당되지 않는 조건]
        return 0
print(sorted(l,key=cmp_to_key(comparator)))
# print(sorted(l,key=cmp_to_key(comparator), reverse=True)) #결과값 뒤집기