class Node:
    pass

def insert(p, x):
    if p is None:
        q = Node()
        q.val = x
        q.lch = q.rch = None

        return q
    else:
        if x < p.val:
            p.lch = insert(p.lch, x)
        else:
            p.rch = insert(p.rch, x)

        return p

def find(p, x):
    if p is None:
        return False
    elif x == p.val:
        return True
    elif x < p.val:
        return find(p.lch, x)
    else:
        return find(p.rch, x)

def remove(p, x):
    if p is None:
        return None
    elif x < p.val:
        p.lch = remove(p.lch, x)
    elif x > p.val:
        p.rch = remove(p.rch, x)
    elif p.lch is None:
        q = p.rch
        p = q
    elif p.lch.rch is None:
        q = p.lch
        q.rch = p.rch
        p = q
    else:
        q = p.lch
        while q.rch is not None and q.rch.rch is not None:
            q = q.rch

        r = q.rch
        q.rch = r.lch
        r.lch = p.lch
        r.rch = p.rch
        p = r

    return p

p = insert(None, 7)
p = insert(p, 2)
p = insert(p, 1)
p = insert(p, 15)
p = insert(p, 10)
p = insert(p, 11)
p = insert(p, 8)
p = insert(p, 17)
p = insert(p, 16)
p = insert(p, 19)
p = remove(p, 15)
print(p.val)
