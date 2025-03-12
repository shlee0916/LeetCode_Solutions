'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        result = []

        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        result = list(cnt.items())
        result.sort(key = lambda x: -x[1])
        
        return [key for key, val in result[:k]]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.topKFrequent(nums = [1, 1, 1, 2, 2, 3], k = 2)
    print(test1, [1, 2])
    assert test1 == [1, 2]
    
    test2 = sol.topKFrequent(nums = [1], k = 1)
    print(test2, [1])
    assert test2 == [1]
    