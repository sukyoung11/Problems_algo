import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()

    max = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max:
            max = cnt

    print(f'#{t+1} {max}')


"""
# 딕셔너리 이용
    dic = {}
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt+=1
        dic[i] = cnt

    print(max(dic.values()))
    """

