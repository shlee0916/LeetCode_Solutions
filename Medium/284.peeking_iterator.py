'''
https://leetcode.com/problems/peeking-iterator/description/
'''

from typing import List


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums: List[int]):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.iter = nums
        self.pointer = 0
        

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.pointer < len(self.iter):
            return True
        else:
            return False
    

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            ret = self.iter[self.pointer]
            self.pointer += 1
        else:
            ret = None
        
        return ret


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cur = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur


    def next(self):
        """
        :rtype: int
        """
        ret = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None
        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.cur != None
        

if __name__ == "__main__":
    iter = Iterator([1, 2, 3])
    peek_iter = PeekingIterator(iter)
    
    assert peek_iter.next() == 1
    assert peek_iter.peek() == 2
    assert peek_iter.hasNext() == True
    assert peek_iter.next() == 2
    assert peek_iter.next() == 3
    assert peek_iter.hasNext() == False


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].