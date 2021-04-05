"""
Design your implementation of the circular queue. The circular queue is a linear data structure
in which the operations are performed based on FIFO (First In First Out) principle and the last
position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the
queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if
there is a space in front of the queue. But using the circular queue, we can use the space to store
new values.

Status: Incomplete. Will come round to this in a bit
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.cir_que = [None]*k
        self.start = 0
        self.end = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if (self.end - self.start + 1) % self.k:
            self.cir_que[self.end] = value
            self.end = (self.end + 1) % self.k
            return True
        return False


    def deQueue(self) -> bool:
        if self.start != self.end:
            self.cir_que[self.end] = None
            self.end = (self.end - 1) % self.k
            return True
        return False

    def Front(self) -> int:
        return self.cir_que[self.start]

    def Rear(self) -> int:
        return self.cir_que[self.end]

    def isEmpty(self) -> bool:
        return self.start == self.end

    def isFull(self) -> bool:
        return  ((self.end - self.start + 1) % self.k) == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()