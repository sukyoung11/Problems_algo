import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    words=[input() for _ in range(5)]
    max_len = max(map(len,words))

    for i in range(len(words)):
        blank = max_len - len(words[i])
        words[i]+=' '*blank

    result = []
    for col in range(max_len):
        for row in range(5):
            result.append(words[row][col])
    print(f'#{t+1} {("").join(result).replace(" ","")}')

    """
 max() 안쓰고 max_len 구하기
    max_len = 0
    for word in words:
        if len(word)>max_len:
            max_len = len(word)
    """