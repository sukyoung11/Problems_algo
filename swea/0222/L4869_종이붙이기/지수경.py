import sys
sys.stdin = open('input.txt')

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

T = int(input())
for t in range(T):
    N = int(input())
    answer = 0
    for paper_20 in range(1,(N//20)+1):
        paper_10 = (N - 20*paper_20)//10
        answer += (factorial(paper_20 + paper_10)//(factorial(paper_20)*factorial(paper_10)))*(2**paper_20)
    print(f'#{t+1} {answer+1}')


