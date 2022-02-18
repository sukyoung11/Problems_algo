import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    counts = [0 for _ in range(12)]
    
    for number in numbers:
        counts[int(number)] += 1
    
    triplete = run = 0
    for _ in range(2):
        i = 0
        while i < 10:
            if counts[i] == 3:
                triplete += 1
                counts[i] -= 3

            elif counts[i] and counts[i+1] and counts[i+2]:
                run += 1
                counts[i] -= 1
                counts[i+1] -= 1
                counts[i+2] -= 1
            i += 1
            
    if triplete + run == 2:
        print(f'#{tc} Baby-gin!')
    else:
        print(f'#{tc} Wrong')
    
