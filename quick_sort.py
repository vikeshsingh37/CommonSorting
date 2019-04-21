def quick_sort(A):
    A,pi = partition(A)
    if len(A) <= 2:
        return A
    return(quick_sort(A[:pi]) + quick_sort(A[pi:]))

def partition(A):
    cur = i = 0
    pi = len(A) -1
    for cur in range(0,pi):
        if A[cur] <= A[pi]:
            A[cur],A[i] = A[i],A[cur]
            i += 1
    A[pi],A[i] = A[i],A[pi]
    pi = i
    return A,pi