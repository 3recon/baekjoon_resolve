n, m, start = map(int, input().split())

adjList = []
for i in range(1, n + 1):
    adjList.append((i, []))

for i in range(m):
    u, v = map(int, input().split())
    adjList[u - 1][1].append(v)  # for문 두개 합치기
    adjList[v - 1][1].append(u)

for i in range(0, n):
    adjList[i][1].sort()


# dfs
def dfs(graph, vertex, visited=None):
    if visited == None:
        visited = set()

    visited.add(vertex)
    print(vertex,end=" ")

    for neighbor in graph[vertex - 1][1]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph,start):
    visited=set()
    queue=[start]

    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend(graph[vertex-1][1])


dfs(adjList, start)
print()
bfs(adjList, start)
