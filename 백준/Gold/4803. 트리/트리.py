import sys

results = []




while True:

    n, m = map(int, sys.stdin.readline().strip().split())

    if (n,m) == (0,0):
        break
    vertexes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

    uf = [i for i in range(n+1)]
    has_cycle = [False]*(n+1)
    def find(x):
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]

    def union(x,y):
        x = find(x)
        y = find(y)

        if x == y:
            has_cycle[x] = True
            return False
        
        if x > y:
            uf[x] = y
            has_cycle[y] = has_cycle[x] or has_cycle[y]
        else:
            uf[y] = x
            has_cycle[x] = has_cycle[x] or has_cycle[y]

        return True
    
    for x,y in vertexes:
        union(x,y)
    tree_set = set()
    for i in range(1, n+1):
        target = find(i)
        if has_cycle[target]:
            continue
        tree_set.add(target)
    
    results.append(len(tree_set))




        




for idx,result in enumerate(results):
    if result == 0:
        print("Case {}: No trees.".format(idx+1))
    elif result == 1:
        print("Case {}: There is one tree.".format(idx+1))
    else:
        print("Case {}: A forest of {} trees.".format(idx+1,result))