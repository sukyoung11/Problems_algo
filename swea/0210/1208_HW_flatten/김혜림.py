import sys
sys.stdin = open('input.txt')

T = 10
N = 100

# 리스트의 최대 요소의 idx를 반환하는 함수
def get_max_i(list):
    max_v = list[0]
    max_i = 0
    for idx in range(100):          # 가로는 100으로 고정 / len(list)로 접근하면 더 재사용성 높음
        if list[idx] >= max_v:
            max_v = list[idx]
            max_i = idx
    return max_i        

# 리스트의 최소 요소의 idx를 반환하는 함수
def get_min_i(list):
    min_v = list[0]
    min_i = 0
    for idx in range(100):          # 가로는 100으로 고정 / len(list)로 접근하면 더 재사용성 높음
        if list[idx] <= min_v:
            min_v = list[idx]
            min_i = idx
    return min_i  

# 입력받기
for tc in range(1, T+1):
    D = int(input())
    blocks = list(map(int, input().split()))
    
    # 덤프 D회 시행하기
    for idx in range(D):
        blocks[get_max_i(blocks)] -= 1
        blocks[get_min_i(blocks)] += 1
    
    result = blocks[get_max_i(blocks)] - blocks[get_min_i(blocks)]
    print(f'#{tc} {result}')
        