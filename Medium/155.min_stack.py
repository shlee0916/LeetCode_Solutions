'''
https://leetcode.com/problems/min-stack/description/
'''

class MinStack:
    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or cur_min > val:
            cur_min = val

        self.stack.append((val, cur_min))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        val = None
        if self.stack:
            val = self.stack[-1][0]

        return val


    def getMin(self) -> int:
        cur_min = None
        if self.stack:
            cur_min = self.stack[-1][1]

        return cur_min


if __name__ == "__main__":
    stack = MinStack()
    
    assert stack.push(-2) == None
    assert stack.push(0) == None
    assert stack.push(-3) == None

    assert stack.getMin() == -3
    
    assert stack.pop() == None
    
    assert stack.top() == 0
    
    assert stack.getMin() == -2
    
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()