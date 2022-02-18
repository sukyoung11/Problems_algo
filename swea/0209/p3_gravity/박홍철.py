import sys
sys.stdin = open("input.txt")

num_of_falls = int(input())

for fall in range(1, num_of_falls+1):
    edge = int(input())

    boxes = [int(i) for i in input().split()]
    
    posit = 0
    biggest = boxes[0]
    max_fall = 0

    for i in range(1, edge):
        if biggest <= boxes[i]:
            max_fall = i - posit if i - posit >= max_fall else max_fall
            posit = i
            biggest = boxes[i]

    max_fall = edge - posit if edge - posit > max_fall else max_fall

    print(f'#{fall} {max_fall}')
