import sys
sys.stdin = open('input.txt')


def dfs(V, E, graph, S, G):
    visited = [False for _ in range(V+1)]
    to_visits = [S]

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            to_visits += graph[current]

    return visited[G]



T = int(input())
for t in range(T):
    V, E = map(int,input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int,  input().split())
        graph[start].append(end)

    S, G = map(int,input().split())

    print(graph)
