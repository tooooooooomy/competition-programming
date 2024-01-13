
def solution(A):
    # write your code in Python 3.6
    N = len(A)

    def helper(left, right):
        if left % 2 + right % 2 == 1:
            t1, t2 = A[left], A[right]

            while left > 0 and right < N-1 and A[left-1] == t2 and A[right+1] == t1:
                left -= 1
                right += 1
                t1, t2 = t2, t1
        else:
            t1, t2 = A[left], float('inf')
            while left > 0 and right < N-1 and A[left-1] == A[right+1]:
                if t2 == float('inf'):
                    t2 = A[left-1]
                
                if A[left] != t1 or A[left-1] != t2:
                    break
                
                left -= 1
                right += 1
                t1, t2 = t2, t1

        return right - left + 1



    ans = float('-inf')
    for i in range(N):
        tmp = helper(i, i)
        ans = max(ans, tmp)
        if i < N-1:
            tmp = helper(i, i+1)
            ans = max(ans, tmp)

    return ans

a = [7,4,2,4,2,-9]
b = [7, -5, -5, -5, 7, -1, 7]
c = [1]
print(solution(a))
# print(solution(b))
# print(solution(c))
