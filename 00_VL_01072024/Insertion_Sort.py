
# Was macht diese Funktion ? 
# Was muss bei "?" eingefügt werden ?
# Laufzeitkomplexität ?

'''
def meinefunktion(arr):
    for i in range(i, len(arr)):
        key = arr[i]
        j = i - 1
        while j  => 0 and key = ? arr[i]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
'''

# meinefunktion = Insetion Sort
# Laufzeitkomplexität = O(n^2)
# Weil = Schleife/n immer durchlaufen werden, auch wenn das Array schon sortiert ist

def meinefunktion(arr):
    for i in range(i, len(arr)):
        key = arr[i]
        j = i - 1
        while j  >= 0 and key > arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

