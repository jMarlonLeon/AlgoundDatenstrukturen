# FIFO

# Nutzung einer Liste als Warteschlange, hinzufuegen der Warteschlangen-Klasse
from collections import deque

# Erzeugen einer Warteschlange
queue = deque([])

# Anfügen von Elementen (Enqueue-Operation)
queue.append('a')
queue.append('b')
queue.append('c')

print("Queue: ", queue)

# Dequeue-Operation über popleft
temp = queue.popleft()
print(temp ,"entfernt")
print("Queue: ", queue)

# Alle Elemente der Queue entfernen
laenge = len(queue)
for i in range(laenge):
    temp = queue.popleft()
    print(temp, "entfernt")
    print("Queue: ", queue)