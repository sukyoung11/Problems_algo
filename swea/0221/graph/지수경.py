import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        start, end = map(int,input().split())
        graph[start].append(end)

    S, G = map(int,input().split())


    print(graph)

