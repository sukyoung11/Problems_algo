import sys
sys.stdin = open('input.txt')


def dfs():
    # 특정 node에 방문했는지 체크용
    visited = [False for _ in range(V+1)]
    # 앞으로 방문할 곳을 모아 놓은 Stack
    to_visits = [S]

    while to_visits:
        current = to_visits.pop()
        print(current, end='=>')
        if not visited[current]:
            visited[current] = True
            if current == G:
                return visited[G]

            to_visits += graph[current]

    return visited[G]


T = int(input())

for tc in range(1, T+1):
    # V 정점의 개수, E 간선의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    print(dfs())