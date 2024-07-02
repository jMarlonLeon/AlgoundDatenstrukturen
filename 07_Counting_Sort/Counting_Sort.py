
def counting_sort(A,B,n,k):
    C = [0] * (k+1)
    for j in range(n):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()
print("Unsortiertes Array:", start)

sortiert = counting_sort(eingabe, [0] * len(eingabe), len(eingabe), max(eingabe))
print("Sortiertes Array:", sortiert)

# A = Eingabe-Array
# B = Ausgabe-Array
# n = Anzahl der Elemente in A
# k = Größtes Element in A
