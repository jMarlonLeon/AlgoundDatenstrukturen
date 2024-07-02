def build_max_heap(A,n):
    for i in range(n//2-1,-1,-1):
        max_heapify(A,i,n)
    
def max_heapify(A,i,n):
    l = 2*i+1
    r = 2*i+2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,largest,n)

def heap_sort(A,n):
    build_max_heap(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        max_heapify(A,0,i)
    

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()
print("Unsortiertes Array:", start)

heap_sort(eingabe, len(eingabe))
print("Sortiertes Array:", eingabe)