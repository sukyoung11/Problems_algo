import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    N = int(input())
    rooms = [list(map(int,input().split())) for _ in range(N)]
    room_sort = list(map(sorted,rooms))

    corr = [0]*200
    for room in room_sort:
        if room[0] % 2:
            start = room[0]//2
        else:
            start = room[0]//2-1

        if room[1] % 2:
            end = room[1]//2
        else:
            end = room[1]//2-1

        for i in range(start,end+1):
          corr[i] +=1

    print(f'#{t+1} {max(corr)}')


"""
ㅠㅠ
T = int(input())
for t in range(T):
    N = int(input())
    rooms = [list(map(int,input().split())) for _ in range(N)]
    room_minmax = list(map(sorted,rooms))
    room_sort = sorted(room_minmax)


    time = 0
    for i in range(len(room_sort)):
        cnt = 0
        if (room_sort[i][0]%2) == 0 and (room_sort[i][1]%2) == 0:  # 짝짝
            for j in range(i+1,len(room_sort)):
                if room_sort[j][0]> room_sort[i][1]:
                    cnt += 1
            for j in range(0,i):
                if room_sort[j][1] < room_sort[i][0] -1:
                    cnt+=1

        elif (room_sort[i][0]%2) == 1 and (room_sort[i][1]%2) == 0:  # 홀짝
            for j in range(i+1,len(room_sort)):
                if room_sort[j][0]> room_sort[i][1]:
                    cnt += 1
            for j in range(0,i):
                if room_sort[j][1] < room_sort[i][0]:
                    cnt+=1

        elif (room_sort[i][0]%2) == 0 and (room_sort[i][1]%2) == 1:  # 짝홀
            for j in range(i+1,len(room_sort)):
                if room_sort[j][0]> room_sort[i][1]+1:
                    cnt += 1
            for j in range(0,i):
                if room_sort[j][1] < room_sort[i][0]-1:
                    cnt+=1
        else:  # 홀홀
            for j in range(i + 1, len(room_sort)):
                if room_sort[j][0] > room_sort[i][1]+1:
                    cnt += 1
            for j in range(0, i):
                if room_sort[j][1] < room_sort[i][0]:
                    cnt += 1


        if len(room_sort) -1 == cnt:
            time+=1

    if time == 0:
        result = N
    elif time ==N:
        result = 1
    else:
        result = N-time

    print(f'#{t+1} {result}')
"""