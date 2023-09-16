'''
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
'''

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for oper in operations:
            if "+" in oper: ans += 1
            elif "-" in oper: ans -= 1

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.finalValueAfterOperations(operations = ["--X", "X++", "X++"])
    assert test1 == 1
    
    test2 = sol.finalValueAfterOperations(operations = ["++X", "++X", "X++"])
    assert test2 == 3
    
    test3 = sol.finalValueAfterOperations(operations = ["X++", "++X", "--X", "X--"])
    assert test3 == 0
    