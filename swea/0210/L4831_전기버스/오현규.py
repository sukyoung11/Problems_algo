import sys
sys.stdin = open('input.txt')
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N*2)]

print(arr)

# print(arr[0], arr[1]) => [3, 10, 5] [1, 3, 5, 7, 9]
# print(len(arr)) => 8
in_list_value = range(1, int(len(arr)/2)+1)  # 1, 2, 3, 4

for idx in in_list_value:
    temp_idx = (2 * idx) - 1  # => 1, 3, 5, 7 (리스트 고르기에 필요한 인덱스)
    new_list = []
    new_list.append(arr[temp_idx][0])


    for _ in range(len(arr[temp_idx]) - 1):
        temp = arr[temp_idx][_+1] - arr[temp_idx][_]
        new_list.append(temp)

    # print(new_list)

    # print(arr[temp_idx-1][0])  # 3, 3, 5, 5 (K값)
    # print(arr[temp_idx][0])  # 1, 1, 4, 6 (리스트 첫 값)
    # print(new_list)

    temp_value = 0
    cnt = 0

    for _ in new_list:
        if arr[temp_idx][0] > arr[temp_idx-1][0]:
            cnt = 0

        elif _ > arr[temp_idx-1][0]:
            cnt = 0

        else:
            temp_value += _
            if temp_value == arr[temp_idx - 1][0]:
                temp_value = 0
                cnt += 1
            elif temp_value > arr[temp_idx - 1][0]:
                temp_value = 0
                cnt += 2

    print(f'#{idx} {cnt}')
    #
    # num = 1
    # while num <= len(cnt)/2:
    #     print(f'#{num} {cnt}')
    #     num += 1