'''
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02
'''

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        left_chalks = k % sum(chalk)
        
        for idx, num in enumerate(chalk):
            if left_chalks >= num:
                left_chalks -= num
            else:
                break

        return idx
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.chalkReplacer(chalk = [5, 1, 5], k = 22)
    assert test1 == 0

    test2 = sol.chalkReplacer(chalk = [3, 4, 1, 2], k = 25)
    assert test2 == 1
    