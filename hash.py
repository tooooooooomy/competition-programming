class Hash:
    def __init__(self, size=4):
        self.arrays = [[] for _ in range(size)]

    def index(self, key):
        return hash(key) % len(self.arrays)

    def get(self, key):
        i = self.index(key)

        print(self.arrays)
        for comb in self.arrays[i]:
            if comb[0] == key:
                return comb[1]

        return None

    def set(self, key, value):
        if self.is_full():
            self.double()

        i = self.index(key)

        self.arrays[i].append([key, value])


    def is_full(self):
        c = 0

        for arr in self.arrays:
            if len(arr) > 0:
                c += 1

        return c >= len(self.arrays) // 2

    def double(self):
        new_arrays = [[] for _ in range(len(self.arrays)*2)]
        for arr in self.arrays:
            for key, val in arr:
                i = hash(key) % (len(self.arrays) * 2)
                new_arrays[i].append([key, val])

        self.arrays = new_arrays

myhash = Hash(2)
myhash.set('a', 'hoge')
print(myhash.get('a'))
print(myhash.get('b'))
myhash.set('b', 'fuga')
myhash.set('c', 'hogefuga')

print(myhash.get('a'))
print(myhash.get('b'))
print(myhash.get('c'))
