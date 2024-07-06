def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

# Wie funktioniert die Rekursion bei merge_sort?
# merge_sort([3,6,1,7,5,2,9,8], 0, 7)

# merge_sort([3,6,1,7], 0, 3)
    # merge_sort([3,6], 0, 1)
        # merge_sort([3], 0, 0)
        # merge_sort([6], 1, 1)
            # merge([3,6], 0, 0, 1)
    # merge_sort([1,7], 0, 1)
        # merge_sort([1], 0, 0)
        # merge_sort([7], 1, 1)
            # merge([1,7], 0, 0, 1)
    # merge([3,6,1,7], 0, 1, 3)

# merge_sort([5,2,9,8], 4, 7)
    # merge_sort([5,2], 4, 5)
        # merge_sort([5], 4, 4)
        # merge_sort([2], 5, 5)
        # merge([2,5], 4, 4, 5)
    # merge_sort([9,8], 6, 7)
        # merge_sort([9], 6, 6)
        # merge_sort([8], 7, 7)
            # merge([8,9], 6, 6, 7)

# merge([2,5,8,9], 4, 5, 7)
# merge([1,3,6,7,2,5,8,9], 0, 3, 7)
# [1,2,3,5,6,7,8,9]

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    # Erstelle Hilfsarrays L und R
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    
    for i in range(n1):
        L[i] = A[p + i]
    
    for j in range(n2):
        R[j] = A[q + j + 1]
    
    # Setze Wächterelemente
    L[n1] = float('inf')
    R[n2] = float('inf')
    
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

print("Unsortiertes Array:", start)

merge_sort(eingabe, 0, len(eingabe) - 1)
print("Sortiertes Array:", eingabe)