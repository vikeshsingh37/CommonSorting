def bubble_sort(A):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                A[i],A[j] = A[j],A[i]
    return(A)