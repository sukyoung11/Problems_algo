import sys
sys.stdin = open('input.txt')

# greedy-algorithm으로 접근하기!

# TC 개수 받아오기
T = int(input())

for tc in range(1, T+1):
    numbers = input()
    counts = [0]*12
    
    # counts에 숫자별 개수 채우기
    for number in numbers:
        counts[int(number)] += 1
    
    # triplete, run 찾기 (run이 두번있는 경우 해결이 안됨 -> 두번 돌아야 하나)
    triplete = run = 0
    for _ in range(2):
        idx = 0
        while idx < 10:
            if counts[idx] == 3:
                triplete += 1
                counts[idx] -= 3
            elif counts[idx] and counts[idx+1] and counts[idx+2]:
                run += 1
                counts[idx] -= 1
                counts[idx+1] -= 1
                counts[idx+2] -= 1
            idx += 1
            
    if triplete + run == 2:
        answer = 'Baby-gin!'
    else:
        answer = 'Wrong'
    print(f'#{tc} {answer}')