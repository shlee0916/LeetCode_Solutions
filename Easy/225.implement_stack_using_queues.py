'''
https://leetcode.com/problems/implement-stack-using-queues/
'''
from collections import deque


class MyStack:

    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)
        for _ in range(len(self.deq) - 1):
            self.deq.append(self.deq.popleft())

    def pop(self) -> int:
        return self.deq.popleft()

    def top(self) -> int:
        return self.deq[0]

    def empty(self) -> bool:
        if not self.deq:
            return True
        return False


if __name__ == "__main__":
    stack = MyStack()

    stack.push(1)
    stack.push(2)

    print(stack.pop())
    print(stack.top())

    print(stack.empty())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()