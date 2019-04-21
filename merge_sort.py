def merge_sort(A):
    if len(A) <= 1:
        return(A)
    mid = len(A)//2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left,right)

def merge(left,right):
    i = j = 0
    out = []
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1 
    
    out += left[i:]
    out += right[j:]
    return out