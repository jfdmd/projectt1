# This code creates a Queue class
class Queue:
    def __init__(self):
        self.queue = list()

    def push_to_queue(self, queue_value):
# Insert method to add element to the queue
        if queue_value not in self.queue:
            self.queue.insert(0,queue_value)
            return True
        return False

    def size_of_queue(self):
        return len(self.queue)

    # Pop method to remove element from the queue
    def pop_from_queue(self):
        if len(self.queue) > 0:
            return self.queue.pop()

        return ("No elements in Queue!")

# TheQueue = Queue()
# TheQueue.push_to_queue("Mon")
# TheQueue.push_to_queue("Tue")
# TheQueue.push_to_queue("Wed")
# print(TheQueue.size_of_queue())
# print(TheQueue.pop_from_queue())
# print(TheQueue.pop_from_queue())