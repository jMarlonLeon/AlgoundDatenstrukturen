# FIFO

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.queue)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue:", list(q.queue))  # Output: Queue: [1, 2, 3]
print("Dequeued:", q.dequeue())  # Output: Dequeued: 1
print("Queue after dequeue:", list(q.queue))  # Output: Queue after dequeue: [2, 3]