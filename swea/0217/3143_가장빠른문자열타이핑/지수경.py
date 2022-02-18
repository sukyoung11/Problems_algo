import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    sentence, word = input().split()

    cnt = 0
    i = 0
    while i <= len(sentence)-len(word):
        if sentence[i:i+len(word)] == word:
            cnt += 1
            i = i+len(word)
        else:
            i += 1

    result = (len(sentence) - cnt * (len(word))) + cnt
    print(result)





