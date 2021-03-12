class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min_heap = []

    def push(self, x: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
r = [-2,-1,7,4,-2,0]
for item in r:
    obj.push(item)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()