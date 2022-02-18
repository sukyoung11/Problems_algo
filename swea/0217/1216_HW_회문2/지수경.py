import sys
sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1,11):
    N = int(input())
    letters = [list(input()) for _ in range(100)]

    max = 0
    for row in range(0,100):  # 행 탐색
        for i in range(1,99):
            j = 1
            cnt = 0
            ans = 0
            while 1:
                # 회문 길이가 짝수일 때
                if letters[row][i] == letters[row][i+1]:
                    if ((i-j) >= 0 and (i+j+1) < 100) and (letters[row][i-j] == letters[row][i+j+1]):
                        j += 1
                        cnt += 1
                        ans = cnt*2 +2
                    else:
                        if ans >= max:
                            max = ans
                        break

                # 회문 길이가 홀수일 때
                elif ((i-j) >= 0 and (i+j) < 100) and (letters[row][i-j] == letters[row][i+j]):
                    j += 1
                    cnt+=1
                    ans = cnt*2+1

                else:
                    if ans >= max:
                        max = ans
                    break

    for col in range(0,100):  # 열 탐색 ( 행 코드와 같음)
        for i in range(1,99):
            j = 1
            cnt = 0
            ans = 0
            while 1:
                if letters[i][col] == letters[i+1][col]:
                    if ((i-j) >= 0 and (i+j+1) < 100) and (letters[i-j][col] == letters[i+j+1][col]):
                        j += 1
                        cnt += 1
                        ans = cnt*2 + 2
                    else:
                        if ans >= max:
                            max = ans
                        break

                elif ((i-j) >= 0 and (i+j) < 100) and (letters[i-j][col] == letters[i+j][col]):
                    j += 1
                    cnt+=1
                    ans = cnt*2 + 1

                else:
                    if ans >= max:
                        max = ans
                    break

    print(f'#{t} {max}')