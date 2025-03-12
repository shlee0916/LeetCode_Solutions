'''
https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2023-09-13
'''

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ans = [1] * length

        for idx in range(length - 1):
            if ratings[idx] < ratings[idx + 1]:
                ans[idx + 1] = max(ans[idx] + 1, ans[idx + 1])

        for idx in range(length - 2, -1, -1):
            if ratings[idx + 1] < ratings[idx]:
                ans[idx] = max(1 + ans[idx + 1], ans[idx])

        return sum(ans)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.candy(ratings = [1, 0, 2])
    assert test1 == 5
    
    test2 = sol.candy(ratings = [1, 2, 2])
    assert test2 == 4
    