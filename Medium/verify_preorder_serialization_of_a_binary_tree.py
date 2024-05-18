'''
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        null_nodes = 1

        for node in preorder.split(","):
            if null_nodes == 0:
                return False

            if node.isdigit():
                null_nodes += 1
            else:
                null_nodes -= 1

        return null_nodes == 0
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isValidSerialization(preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#")
    assert test1 == True
    
    test2 = sol.isValidSerialization(preorder = "1,#")
    assert test2 == False
    
    test3 = sol.isValidSerialization(preorder = "9,#,#,1")
    assert test3 == False
    