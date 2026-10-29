class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length() + 1

        tin = [0] * n
        tout = [0] * n
        dep = [0] * n
        up = [[0] * n for _ in range(LOG)]
        bit = [0] * (n + 2)
        timer = [0]

        def dfs(u, p):
            timer[0] += 1
            tin[u] = timer[0]
            up[0][u] = p

            for j in range(1, LOG):
                up[j][u] = up[j - 1][up[j - 1][u]]

            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)

            tout[u] = timer[0]

        def add(i, x):
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def update(u, x):
            add(tin[u], x)
            add(tout[u] + 1, x)

        def summ(i):
            x = 0
            while i > 0:
                x ^= bit[i]
                i -= i & -i
            return x

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u

            diff = dep[u] - dep[v]

            for j in range(LOG - 1, -1, -1):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        dfs(0, 0)
        s = list(s)

        for u in range(n):
            update(u, 1 << (ord(s[u]) - ord('a')))

        ans = []

        for q in queries:
            a = q.split()
            u = int(a[1])

            if a[0] == "update":
                c = a[2]

                old_mask = 1 << (ord(s[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                update(u, old_mask ^ new_mask)
                s[u] = c

            else:
                v = int(a[2])
                w = lca(u, v)

                mask = (
                    summ(tin[u])
                    ^ summ(tin[v])
                    ^ (1 << (ord(s[w]) - ord('a')))
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans