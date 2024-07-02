
def insertion_sort(array, length):
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

ausgabe = insertion_sort(start, len(eingabe))

print(eingabe)

print(ausgabe)