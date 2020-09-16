V = 4
color = [0]*4

def dfs(v, c):
    print("1")
    color[v] = c
    for i in range(len(G[v])):
        print(G[v][i])
        print(color[G[v][i]])
        if color[G[v][i]] == c:
            return False
        
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False

    return True

def solve():
    for i in range(V):
        if color[i] == 0:
            if not dfs(i, 1):
                print("No\n")
                return

    print("Yes\n")


G = [[] for i in range(V)]
G[0].append(1)
G[0].append(3)
G[1].append(0)
G[1].append(2)
G[2].append(1)
G[2].append(3)
G[3].append(0)
G[3].append(2)

solve()
