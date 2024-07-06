
def insertion_sort(array, length):
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

start = [3,1,5,7,2,9,6]
eingabe = start.copy()

print("Unsortiertes Array:", start)

insertion_sort(eingabe, len(eingabe))
print("Sortiertes Array:", eingabe)