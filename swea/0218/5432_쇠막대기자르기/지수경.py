import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    array = list(input())
    for i in range(len(array)-1):
        if array[i]=='(' and array[i+1] ==')':
            array[i] = 0
            array[i+1] = 0

    cnt = 0
    j = 0
    result = []
    while j < len(array):
        if '(' not in array:
            break
        if array[j]=='(':
            cnt=0
            j+=1
        elif array[j]==0:
            cnt+=1
            j+=1
        elif array[j]==')':
            result.append(cnt)
            del array[j]
            del array[j-cnt-1]
            cnt = 0
            j=0

    print(f'#{t+1} {sum(result)//2+len(result)}')




