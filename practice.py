from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(int)
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.rank[x] = 0

        if self.parents[x] == x:
            return x

        self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def unite(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return

        if self.rank[par_x] < self.rank[par_y]:
            self.parents[par_x] = par_y
        else:
            if self.rank[par_x] == self.rank[par_y]:
                self.rank[par_x] += 1

            self.parents[par_y] = self.parents[par_x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

u = UnionFind()

print(u.find(1))
print(u.find(2))

u.unite(1, 2)
print(u.find(1))
print(u.find(2))

print(u.same(1, 2))
print(u.same(1, 3))
u.unite(1, 3)
print(u.find(3))
print(u.same(1, 3))
