def quicksort (A, lo, hi):
    if lo < hi:
        p = partition(A, low, hi)

def partition(A ,lo, hi):
    pivot = A[hi]
    i = lo -1
    for j in range(lo,hi-1):
        if A[j] < pivot:
            i+= 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i + 1] = hi
    hi = temp
    return i + 1

    A = [1,3,6,10,100,10000,4,2,60,100]
    print(quicksort(A, 1, 10000))
