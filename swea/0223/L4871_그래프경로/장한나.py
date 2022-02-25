import sys
sys.stdin = open("input.txt")

T = int(input())

# STACK VER.
"""
def dfs(V, E, graph, S, G):
    # 특정 노드 방문 여부
    visited = [False for _ in range(V+1)]
    to_visits = [S]  # 방문할 곳

    while to_visits:  # to_visits에 값이 있으면
        current = to_visits.pop()
        # print(current, end=" => ")
        if not visited[current]:  # 방문해야 할 곳인데 방문한 적이 없다면
            print(current, end=" => ")
            visited[current] = True  # 거기 가보자
                # if current == G:
                    # return visited[G]  # 이게 백트래킹
            to_visits += graph[current]  # 간 곳에서 갈 수 있는 곳을 방문해야 할 곳에 넣는 거

    return visited[G]  # G에 방문한 적이 있니? T/F


for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점, 간선
    graph = [[] for _ in range(V+1)]  # 0도 있어서

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    print(dfs(V, E, graph, S, G))
"""


# ===============================================================
# RECURSIVE VER.

def go(v):
    # print(v, end=" => ")
    visited[v] = True
    # if visited[G]:
    #     return  # 이거 하면 백트래킹이 된다
    for new_v in graph[v]:
        if not visited[new_v]:
            go(new_v)


for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 정점, 간선
    graph = [[] for _ in range(V + 1)]  # 0도 있어서

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())
    visited = [False for _ in range(V+1)]

    go(S)
    print(visited[G])
