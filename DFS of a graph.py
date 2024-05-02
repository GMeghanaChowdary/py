def initiateDFS(node, visited, adj, result):
    result.append(node)
    visited[node] = True

    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFS(neighbour, visited, adj, result)


def printDFSTraversal(adj, n):
    result = []
    visited = [False] * (n+1)

    for i in range(1,n+1):
        if visited[i] == False:
            initiateDFS(i, visited, adj, result)
    for i in range(n):
        print(result[i],end=" ")


# adjacency list construction

n, m = map(int, input().split())
adj = []
for i in range(n+1):
    adj.append([])

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

printDFSTraversal(adj, n)
