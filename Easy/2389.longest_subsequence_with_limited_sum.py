'''
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
'''

from typing import List
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(target: int, target_list: List[int]) -> int:
            left = 0
            right = len(prefix) - 1
            tmp_ans = -1
            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] == query:
                    return mid + 1
                elif prefix[mid] > query:
                    tmp_ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
        
            return len(prefix) if tmp_ans == -1 else tmp_ans
        
        ans = []

        nums.sort()
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)

        for query in queries:
            ans.append(binary_search(query, queries))

        return ans
    
    
    def shortAnswerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = list(accumulate(sorted(nums)))
        return [bisect_right(prefix, query) for query in queries]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.answerQueries(nums = [4, 5, 2, 1], queries = [3, 10, 21])
    print(test1, [2, 3, 4])
    assert test1 == [2, 3, 4]
    
    test2 = sol.answerQueries(nums = [2, 3, 4, 5], queries = [1])
    print(test2, [0])
    assert test2 == [0]
    
    # Short test
    test1 = sol.shortAnswerQueries(nums = [4, 5, 2, 1], queries = [3, 10, 21])
    print(test1, [2, 3, 4])
    assert test1 == [2, 3, 4]
    
    test2 = sol.shortAnswerQueries(nums = [2, 3, 4, 5], queries = [1])
    print(test2, [0])
    assert test2 == [0]
    