class MinStack:

    def __init__(self):
        self.items= []
        

    def push(self, val: int) -> None:
        self.items.append(val)
        

    def pop(self) -> None:
        if len(self.items)!=0:
            self.items.pop()
        else:
            return null

    def top(self) -> int:
        if len(self.items)!=0:
            return self.items[-1]
        else:
            return null
        

    def getMin(self) -> int:
        minimum= min(self.items)
        return minimum

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()