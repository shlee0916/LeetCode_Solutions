'''
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/?envType=daily-question&envId=2024-05-30
'''

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        for i_idx in range(len(arr)):
            cur_xor = arr[i_idx]

            for k_idx in range(i_idx + 1, len(arr)):
                cur_xor ^= arr[k_idx]
                if cur_xor == 0:
                    ans += k_idx - i_idx

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countTriplets(arr = [2, 3, 1, 6, 7])
    assert test1 == 4
    
    test2 = sol.countTriplets(arr = [1, 1, 1, 1, 1])
    assert test2 == 10
    
        