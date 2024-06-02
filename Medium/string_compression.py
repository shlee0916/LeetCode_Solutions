'''
https://leetcode.com/problems/string-compression/description/
'''

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            chars[left] = chars[right]
            cnt = 1

            while right + 1 < len(chars) and chars[right] == chars[right + 1]:
                right += 1
                cnt += 1

            if cnt > 1:
                for ch in str(cnt):
                    chars[left + 1] = ch
                    left += 1

            left += 1
            right += 1

        return left


if __name__ == "__main__":
    sol = Solution()
    
    test1_case = ["a", "a", "b", "b", "c", "c", "c"]
    test1 = sol.compress(chars = test1_case)
    assert test1_case[:test1] == ["a", "2", "b", "2", "c", "3"]

    test2_case = ["a"]
    test2 = sol.compress(chars = test2_case)
    assert test2_case[:test2] == ["a"]
    
    test3_case = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    test3 = sol.compress(chars = test3_case)
    assert test3_case[:test3] == ["a", "b", "1", "2"]
    