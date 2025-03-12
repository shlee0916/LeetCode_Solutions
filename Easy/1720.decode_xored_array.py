'''
https://leetcode.com/problems/decode-xored-array/description/
'''

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.decode(encoded = [1, 2, 3], first = 1)
    assert test1 == [1, 0, 2, 1]
    
    test2 = sol.decode(encoded = [6, 2, 7, 3], first = 4)
    assert test2 == [4, 2, 0, 7, 4]
    