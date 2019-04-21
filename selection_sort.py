def selection_sort(A):
    for i in range(0,len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i],A[min_idx] = A[min_idx],A[i]
    return A