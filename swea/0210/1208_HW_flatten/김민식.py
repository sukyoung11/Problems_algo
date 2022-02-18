import sys
sys.stdin = open('input.txt')


# 가로 길이가 100일때 최고점과 최저점의 인덱스를 찾아서 반환한다.
def get_maxmin_idx(boxes):
    max_idx, min_idx = 0, 0
    for i in range(100):
        if boxes[max_idx] < boxes[i]:
            max_idx = i
        elif boxes[min_idx] > boxes[i]:
            min_idx = i
    return max_idx, min_idx


T = 10
for tc in range(T):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 평탄화 시작 전에 최고점과 최저점을 찾아줘야 한다.
    max_idx, min_idx = get_maxmin_idx(boxes)

    # 덤프 횟수만큼 평탄화 작업
    while dump:
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        dump -= 1

        # 평탄화 작업 후에 최고점과 최저점을 다시 찾아야 한다.
        max_idx, min_idx = get_maxmin_idx(boxes)
        # 덤프 횟수가 남아도 평탄화가 완료되면 중단한다.
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break

    answer = boxes[max_idx] - boxes[min_idx]
    print(f'#{tc + 1} {answer}')
