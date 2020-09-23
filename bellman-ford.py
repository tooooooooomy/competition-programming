es = [
  { "from": 0, "to": 1, "cost": 2 },
  { "from": 0, "to": 2, "cost": 5 },
  { "from": 1, "to": 2, "cost": 4 },
  { "from": 1, "to": 3, "cost": 6 },
  { "from": 1, "to": 4, "cost": 10 },
  { "from": 2, "to": 3, "cost": 2 },
  { "from": 3, "to": 5, "cost": 1 },
  { "from": 4, "to": 6, "cost": 5 },
  { "from": 4, "to": 5, "cost": 3 },
  { "from": 5, "to": 6, "cost": 9 },
]

V = 7
E = 10
d = [9999] * V
print(d)

# the shortest path from s
def shortest_path(s):
    d[s] = 0
    while True:
        update = False
        for i in range(E):
            e = es[i]
            if d[e['from']] is not 9999 and d[e['to']] > d[e['from']] + e['cost']:
                d[e['to']] = d[e['from']] + e['cost']
                update = True

        if not update:
            break

shortest_path(3)

print(d)

def find_negative_loop():
    for i in range(V):
        d[i] = 0

    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e['to']] > d[e['from']] + e['cost']:
                d[e['to']] = d[e['from']] + e['cost']

                if i is V - 1:
                    return True

    return False

print(find_negative_loop())
