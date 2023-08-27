'''
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
'''

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        cnt = 0

        set_a = set()
        set_b = set()
        for a, b in zip(A, B):
            set_a.add(a)
            set_b.add(b)

            if a == b:
                cnt += 1
                ans.append(cnt)
                continue
            
            if a in set_b:
                cnt += 1
            if b in set_a:
                cnt += 1

            ans.append(cnt)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findThePrefixCommonArray(A = [1, 3, 2, 4], B = [3, 1, 2, 4])
    assert test1 == [0, 2, 3, 4]
    
    test2 = sol.findThePrefixCommonArray(A = [2, 3, 1], B = [3, 1, 2])
    assert test2 == [0, 1, 3]
    