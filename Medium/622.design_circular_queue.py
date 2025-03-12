'''
https://leetcode.com/problems/design-circular-queue/
'''

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.front = 0
        self.rear = -1
        self.length = k
        self.que = [0] * self.length

        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.length
            self.que[self.rear] = value
            return True
        else:
            return False


    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False
        if self.front == self.rear:
            self.front, self.rear = 0, -1
            return True
        else:
            self.front = (self.front + 1) % self.length
            return True

        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.que[self.front]
        else:
            return -1
        
        
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.que[self.rear]
        else:
            return -1

        
    def isEmpty(self) -> bool:
        return self.rear == -1

        
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.rear + 1) % self.length == self.front
        

if __name__ == "__main__":
    # Your MyCircularQueue object will be instantiated and called as such:
    que = MyCircularQueue(3)
    print(que.enQueue(1))
    print(que.enQueue(2))
    print(que.enQueue(3))
    print(que.enQueue(4))
    print(que.Rear())
    print(que.isFull())
    print(que.deQueue())
    print(que.enQueue(4))
    print(que.Rear())