'''
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
'''

class CustomStack:

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


if __name__ == "__main__":
    cs = CustomStack(3)
    cs.push(3)
    cs.push(1)
    cs.push(2)
    assert cs.pop() == 2
    cs.push(2)
    cs.push(4)
    assert cs.pop() == 2
    cs.increment(1, 100)
    cs.increment(5, 200)
    assert cs.pop() == 201
    assert cs.pop() == 303
    assert cs.pop() == -1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)