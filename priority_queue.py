
# I took this from the class lecture/discussion slides and coded it in python
class PriorityQueue(object):
    # constructor
    def __init__(self):
        self.queue = []

    # check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # insert an element in the queue
    def insert(self, key):
        self.queue.append(key)

    # returning the last element of the queue
    def pop(self):
        maximum = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[maximum]:
                maximum = i
        item = self.queue[maximum]
        del self.queue[maximum]
        return item
