
def bucket_sort(array):
    n = len(array)
    k = max(array)
    result = []
    buckets = [[] for _ in range(n)]
    
    for i in range(n):
        buckets[int(array[i] * n / (k + 1))].append(array[i])
    
    for i in range(n):
        buckets[i].sort()
    
    for i in range(n):
        result += buckets[i]

    return result

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

print("Unsortiertes Array:", start)

sortiert = bucket_sort(eingabe)
print("Sortiertes Array:", sortiert)