'''
https://leetcode.com/problems/reverse-linked-list/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        nodes = []
        cur_node = head
        while cur_node:
            nodes.append(cur_node)
            cur_node = cur_node.next
            
        for node in nodes:
            node.next = None    
        nodes = nodes[::-1]
        
        new_head = nodes[0]
        cur_node = new_head
        for node in nodes[1:]:
            cur_node.next = node
            cur_node = cur_node.next
            
        return new_head
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))