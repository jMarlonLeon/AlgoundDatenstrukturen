
def counting_sort_einfach(array):
    n = len(array)
    k = max(array)

    C = [0] * (k+1)
    for j in range(n):
        C[array[j]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    B = [0] * n
    for j in range(n-1,-1,-1):
        B[C[array[j]]-1] = array[j]
        C[array[j]] -= 1
    return B

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

print("Unsortiertes Array:", start)

sortiert = counting_sort_einfach(eingabe)
print("Sortiertes Array:", sortiert)
