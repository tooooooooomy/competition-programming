import sys

n = 100
heap = [0] * n
sz = 0

def push(x):
    global heap, sz

    i = sz
    sz += 1

    while i > 0:
        # parent
        p = (i - 1) / 2

        if heap[p] <= x:
            break
        
        heap[i] = heap[p]
        i = p

    heap[i] = x

def pop():
    global heap, sz

    ret = heap[0]

    sz -= 1
    x = heap[sz]

    i = 0
    while(i*2 + 1 < sz):
        a = i * 2 + 1
        b = i * 2 + 2
        if b < sz and heap[b] < heap[a]:
            a = b

        if heap[a] >= x:
            break

        heap[i] = heap[a]
        i = a

    return ret

push(1)
push(5)
push(6)
push(2)
push(10)
push(4)
push(3)

print(heap)

print(pop())
