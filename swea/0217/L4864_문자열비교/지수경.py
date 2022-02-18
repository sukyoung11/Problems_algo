import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
     str1 = input()
     str2 = input()

     if str1 in str2:
          result = 1
     else:
          result = 0

     print(f'#{t+1} {result}')