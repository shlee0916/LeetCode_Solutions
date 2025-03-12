'''
https://leetcode.com/problems/reduce-array-size-to-the-half/
'''
from collections import Counter


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nums = Counter(arr).most_common()
        nums.sort(key = lambda x: -x[1])
        
        length = 0
        for idx, num in enumerate(nums):
            length += num[1]
            if length >= len(arr) // 2:
                return idx + 1
            

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]), 2)