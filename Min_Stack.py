from math import inf


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min_heap = []
        self.min = inf

    def push(self, x: int) -> None:
        self._min_heap.append(x)
        self.min = min(self.min, x)

    def pop(self) -> None:
        return self._min_heap.pop()

    def top(self) -> int:
        return self._min_heap[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
r = [-2,-1,7,4,-2,0]
for item in r:
    obj.push(item)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()