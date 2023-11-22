def find_bridges(adj):
    global timer
    timer = 0
    visited= [False] * len(adj)
    tin = [-1] * len(adj)
    low= [-1] * len(adj)
    bridges = []
    
    def dfs(v, p=-1):
        global timer  # This tells Python to use the 'timer' from the outer scope
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1

        for to in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    # This is a bridge
                    bridges.append((v, to))
    

    for i in range(len(adj)):
        if not visited[i]:
            dfs(i)
    return bridges