'''
https://leetcode.com/problems/design-circular-deque/?envType=daily-question&envId=2024-09-28
'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.__arr = []
        self.__max_size = k


    def insertFront(self, value: int) -> bool:
        if len(self.__arr) + 1 <= self.__max_size:
            self.__arr = [value] + self.__arr
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        if len(self.__arr) + 1 <= self.__max_size:
            self.__arr.append(value)
            return True
        else:
            return False


    def deleteFront(self) -> bool:
        if self.__arr:
            self.__arr = self.__arr[1:]
            return True
        else:
            return False


    def deleteLast(self) -> bool:
        if self.__arr:
            self.__arr = self.__arr[:-1]
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.__arr:
            return self.__arr[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.__arr:
            return self.__arr[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.__arr) == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.__arr) == self.__max_size:
            return True
        else:
            return False
        

if __name__ == "__main__":
    mc = MyCircularDeque(3)
    
    assert mc.insertLast(1) == True
    assert mc.insertLast(2) == True
    assert mc.insertFront(3) == True
    assert mc.insertFront(4) == False
    assert mc.getRear() == 2
    assert mc.isFull() == True
    assert mc.deleteLast() == True
    assert mc.insertFront(4) == True
    assert mc.getFront() == 4


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()