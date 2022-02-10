import sys
sys.stdin = open('input.txt')

T = 10

for case in range(1,T+1):
    row = int(input())
    col = list(map(int,input().split()))
    ans=0
    for i in range(2,len(col)-2):
        group = col[i-2:i+3]
        if col[i] == max(group):
          group.sort()
          result = (group[-1]) - (group[-2])
          ans += result

    print(f'#{case} {ans}')