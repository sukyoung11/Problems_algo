import sys
sys.stdin = open('input.txt', encoding='utf-8')


for t in range(1,11):
    N = int(input())
    search = input()
    sentence = input()

    cnt =0
    for i in range(len(sentence)-len(search)+1):
        if sentence[i:i+len(search)] == search:
            cnt += 1

    print(f'#{t} {cnt}')

