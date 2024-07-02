
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)


start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()  

print("Unsortiertes Array:", start)

quicksort(eingabe, 0, len(eingabe) - 1)
print("Sortiertes Array:", eingabe)