a, b, k = map(int, input().split())

left = a
right = b

while left < min(b, a + k):
    print(left)
    left += 1

s = max(left, right-k+1)
while s <= right:
    print(s)
    s += 1
