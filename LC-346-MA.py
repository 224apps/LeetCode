import queue

class MovingAverage:

    def __init__(self, size):
        self.q =  queue.Queue()
        self.maxSize = size
        self.TotalSum = 0

    def next(self, val):
        if self.q.qsize() == self.maxSize:
            self.TotalSum -= self.q.get()

            self.q.put(val)
            self.TotalSum  += val
            return self.TotalSum / self.q.qsize()