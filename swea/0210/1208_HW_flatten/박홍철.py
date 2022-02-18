import sys
sys.stdin = open("input.txt")

def bubble_sort(elements):
    length = 100

    for i in range(length-1, 0, -1):
        for j in range(i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

def construction(boxes, dumpnum):
    length = 100

    for _ in range(dumpnum):
        boxes[-1] -= 1
        boxes[0] += 1
        for i in range(length-1, 0, -1):
            for j in range(i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
                else:
                    break

        for i in range(length-1):
            for j in range(length-1, i, -1):
                if boxes[j] < boxes[j-1]:
                    boxes[j], boxes[j-1] = boxes[j-1], boxes[j]




num_of_test = 10

for test in range(1, num_of_test+1):
    num_of_dump = int(input()) # 덤프 횟수

    boxes = [int(i) for i in input().split()] # 상자들 높이

    bubble_sort(boxes)

    construction(boxes, num_of_dump)

    print(f'#{test} {boxes[-1] - boxes[0]}')



