'''
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/
'''

class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for num in ["9", "8", "7", "6", "5", "4", "3", "2", "1"]:
            if num in n:
                return int(num)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minPartitions(n = "32")
    assert test1 == 3
    
    test2 = sol.minPartitions(n = "82734")
    assert test2 == 8
    
    test3 = sol.minPartitions(n = "27346209830709182346")
    assert test3 == 9
    