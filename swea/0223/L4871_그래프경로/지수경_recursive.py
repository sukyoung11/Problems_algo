import sys
sys.stdin = open('input.txt')


def go(v):
    visited[v] = True
    for new_v in graph[v]:
        if not visited[new_v]:
            go(new_v)



T = int(input())

for t in range(T):
    V, E = map(int,input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int,  input().split())
        graph[start].append(end)

    S, G = map(int,input().split())
    visited = [False for _ in range(V+1)]
    go(S)

    print(graph)

