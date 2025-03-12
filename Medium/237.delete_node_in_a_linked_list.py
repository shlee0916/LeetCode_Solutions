'''
https://leetcode.com/problems/delete-node-in-a-linked-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


### FOR TEST
class TestClass(Solution):
    def __init__(self):
        self.test_list = ListNode(4)
        self.test_list.next = ListNode(5)
        self.test_list.next.next = ListNode(1)
        self.test_list.next.next.next = ListNode(9)

    
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    
    def test_func(self, node):
        cur_node = self.test_list

        while cur_node:
            if cur_node.val == node.val:
                self.deleteNode(cur_node)
                break
            else:
                cur_node = cur_node.next


    def print_list(self):
        head = self.test_list
        while head:
            print(head.val, end = "")
            head = head.next
        
        print()

if __name__ == "__main__":
    test_class = TestClass()

    test_class.print_list()

    test_class.test_func(ListNode(5))

    test_class.print_list()