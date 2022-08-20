'''
https://leetcode.com/problems/implement-queue-using-stacks/
'''

class MyQueue:
    
    def __init__(self):
        self.in_que = []
        self.out_que = []

    def push(self, x: int) -> None:
        while self.out_que:
            self.in_que.append(self.out_que.pop())
            
        self.in_que.append(x)
        while self.in_que:
            self.out_que.append(self.in_que.pop())

    def pop(self) -> int:
        return self.out_que.pop()

    def peek(self) -> int:
        return self.out_que[-1]

    def empty(self) -> bool:
        if self.out_que:
            return False
        else:
            return True
        
    
if __name__ == "__main__":
    que = MyQueue()
    
    print(que, que.push(1), que.push(2), que.peek(), que.pop(), que.empty())